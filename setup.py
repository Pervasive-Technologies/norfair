# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["norfair"]

package_data = {"": ["*"]}

install_requires = ["filterpy>=1.4.5,<2.0.0"]

setup_kwargs = {
    "name": "norfair",
    "version": "0.3.1",
    "description": "Lightweight Python library for real-time 2D object tracking.",
    "long_description": "Norfair is a customizable lightweight Python library for real-time 2D object tracking. "
    "Using Norfair, you can add tracking capabilities to any detector with just a few lines of code.",
    "author": "Tryolabs",
    "author_email": "hello@tryolabs.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/tryolabs/norfair",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.6,<4.0",
}


setup(**setup_kwargs)
