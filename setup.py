from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="tenorscrap",
    version="0.0.3",
    author="siy",
    author_email="",
    description="Search gif in Tenor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suarasiy/tenorscrap",
    install_requires=["beautifulsoup4", "requests", "lxml"],
    packages=["tenorscrap"]
)