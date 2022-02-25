import setuptools
from anonfiles.main import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="anonfiles",
    version=__version__,
    author="Jak Bin",
    author_email="jakbin4747@gmail.com",
    description="upload and download to anonfiless server",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/redevil1/anonfiless",
    install_requires=["tqdm"],
    python_requires=">=3",
    project_urls={
        "Bug Tracker": "https://github.com/redevil1/anonfiless/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='anonfiles,anonfiles-api,anonfiles-cli,anonymous,upload',
    packages=["anonfiles"],
    entry_points={
        "console_scripts":[
            "anon = anonfiles.main:main"
        ]
    }
)
