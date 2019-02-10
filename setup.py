#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""


# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


requirements = ["Click==7.0", "pyyaml>=4.2b1", "python-gitlab==1.7.0", "gitpython==2.1.11"]

setup_requirements = []

test_requirements = []

setup(
    author="nolte",
    author_email="nolte07@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: German",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Command line utility for handle multiply git projects",
    entry_points={"console_scripts": ["gitlab_bulkcheckout=gitlab_bulkcheckout.cli:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # include_package_data=True,
    # exclude_package_data={"": ["Dockerfile"], "": ["docs"], "": [".travis.yml"]},
    keywords="gitlab_bulkcheckout",
    name="gitlab_bulkcheckout",
    # package_dir={"": "gitlab_bulkcheckout"},
    packages=find_packages(
        include=["gitlab_bulkcheckout"],
        # exclude=["*.circleci", "*Dockerfile", "*.travisci", "*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nolte/gitlab-bulkcheckout",
    version="0.23.0.dev",
    zip_safe=False,
)
