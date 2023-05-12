from setuptools import setup, find_packages
from importlib import util
from os import path
import os

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

spec = util.spec_from_file_location(
    "YOUR_PACKAGE_NAME.__version__", os.path.join("YOUR_PACKAGE_NAME", "__init__.py")
)
mod = util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(mod)  # type: ignore[union-attr]
version = mod.version


setup(
    name='YOUR_PACKAGE_NAME',
    license="MIT License",
    version=version,
    author='AUTHOR_NAME',
    author_email='AUTHOR_EMAIL',
    description='SHORT_DESCRIPTION',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AUTHOR_NAME/YOUR_PACKAGE_NAME',
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'requests',
    ],
    extras_require={
        "dev": [
            "pytest",
            "coverage",
            "mypy",
            "ruff",
        ]
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "YOUR_PACKAGE_NAME=YOUR_PACKAGE_NAME.main:main",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
