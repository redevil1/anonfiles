# anonfiles-script
An upload script for anonfile.com made in python. Supports multiple files.

 [![PyPI version](https://badge.fury.io/py/anonfiles.svg)](https://pypi.org/project/anonfiles/)
 [![Downloads](https://pepy.tech/badge/anonfiles/month)](https://pepy.tech/project/anonfiles)
 [![Downloads](https://static.pepy.tech/personalized-badge/anonfiles?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/anonfiles)
 ![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)


## Installation

```sh
pip3 install anonfiles
```

## Usage 
```sh
anon up {path-to-file_1} {path-to-file _2} ...  # upload file to anonfile server
anon d {url1} {url2} ...              # download file 
```

# API

The anonfile-upload client is also usable through an API (for test integration, automation, etc)

### anonfiles.main.upload([file_path])

```py
from anonfiles.main import upload

upload([file_path])
```
