import os
from setuptools import setup, find_packages

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name = "Text-Summarization",
    version = "0.0.1",
    description = "This is the full Text summarization project",
    author = "Roshil Verma",
    author_email = "roshil.verma.3@gmail.com",
    url = "https://github.com/Roshilv3/Text_Summarization",
    packages = find_packages("requirements.txt")
)