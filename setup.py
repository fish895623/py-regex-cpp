from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ignore-parser",
    version="0.0.1-SNAPSHOT",
    author="fish895623",
    author_email="dan990429+github@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["ignore-parser"],
)
