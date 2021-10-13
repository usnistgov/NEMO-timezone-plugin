from setuptools import setup, find_packages
from os import path

VERSION = "1.0.0"


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NEMO-timezone",
    use_describe_version=True,
    version=VERSION,
    python_requires=">=3.6",
    description="Install multi timezone plugin for NEMO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="NIST Material Measurement Laboratory",
    url="https://www.nist.gov/mml/odi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "NEMO>=3.13.0",
        "django",
        "djangorestframework",
    ],
    license="MIT",
    keywords=["NEMO"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
)
