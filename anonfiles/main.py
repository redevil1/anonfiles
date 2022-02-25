import argparse
import os
from pathlib import Path
from requests import get, post, ConnectionError, head
from requests.exceptions import MissingSchema
import json
import sys
from tqdm import tqdm
from typing import List

__version__ = "1.0.0"
package_name = "anon"
url = 'https://api.anonfiles.com/upload'

def upload(filenames:List[str]):
    for filename in filenames:
        if os.path.isdir(filename):
            print('[ERROR] You cannot upload a directory!')
            break
        else:
            try:
                files = {'file': (open(filename, 'rb'))}
            except FileNotFoundError:
                print(f'[ERROR]: The file "{filename}" doesn\'t exist!')
                break

        print("[UPLOADING]: ", filename)

        try:
            r = post(url, files=files)
        except ConnectionError:
            print("[Error]: No internet")
            return 1

        resp = json.loads(r.text)
        if resp['status']:
            urlshort = resp['data']['file']['url']['short']
            urllong = resp['data']['file']['url']['full']
            print(f'[SUCCESS]: Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
        else:
            message = resp['error']['message']
            errtype = resp['error']['type']
            print(f'[ERROR]: {message}\n{errtype}')

def download(urls:List[str], path: Path=Path.cwd()):
    for url in urls:
        try:
            filesize = int(head(url).headers["Content-Length"])
        except ConnectionError:
            print("[Error]: No internet")
            return 1
        except MissingSchema as e:
            print(e)
            return 1
        filename = os.path.basename(url)
        
        chunk_size = 1024

        try:
            with get(url, stream=True) as r, open(path, "wb") as f, tqdm(
                    unit="B",  # unit string to be displayed.
                    unit_scale=True,  # let tqdm to determine the scale in kilo, mega..etc.
                    unit_divisor=1024,  # is used when unit_scale is true
                    total=filesize,  # the total iteration.
                    file=sys.stdout,  # default goes to stderr, this is the display on console.
                    desc=filename  # prefix to be displayed on progress bar.
            ) as progress:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    datasize = f.write(chunk)
                    progress.update(datasize)
        except ConnectionError:
            return 1
    
example_uses = '''example:
   anon up {files_name}
   anon d {urls}'''

def main(argv = None):
    parser = argparse.ArgumentParser(prog=package_name, description="upload your files on anonfile server", epilog=example_uses, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command")

    upload_parser = subparsers.add_parser("up", help="upload files to https://anonfiles.com")
    upload_parser.add_argument("filename", type=Path, nargs='+', help="one or more files to upload")

    download_parser = subparsers.add_parser("d", help="download files ")
    download_parser.add_argument("filename", nargs='+', type=str, help="one or more URLs to download")
    download_parser.add_argument('-p', '--path', type=Path, default=Path.cwd(), help="download directory (CWD by default)")

    parser.add_argument('-v',"--version",
                            action="store_true",
                            dest="version",
                            help="check version of deb")

    args = parser.parse_args(argv)

    if args.command == "up":
        return upload(args.filename)
    elif args.command == "d":
        return download(args.filename, args.path)
    elif args.version:
        return print(__version__)
    else:
        parser.print_help()

if __name__ == '__main__':
    raise SystemExit(main())
