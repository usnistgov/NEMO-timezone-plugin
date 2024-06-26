from os import path

from setuptools import find_packages, setup

VERSION = "1.3.0"


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NEMO-timezone",
    use_describe_version=True,
    version=VERSION,
    python_requires=">=3.8",
    description="Install multi timezone plugin for NEMO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="NIST Material Measurement Laboratory",
    url="https://www.nist.gov/mml/odi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
        "djangorestframework",
    ],
    extras_require={
        "NEMO-CE": ["NEMO-CE>=2.4.0"],
        "NEMO": ["NEMO>=5.5.0"],
    },
    license="MIT",
    keywords=["NEMO"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
)
