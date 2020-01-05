import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "revolution-wii",
    version = "0.0.1",
    author = "Gideon Tong",
    author_email = "gideon@gideontong.com",
    description = "Video game downloader and organizer for the Nintendo Wii",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://www.github.com/gideontong/revolution",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.8'
)