#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()


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
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Command line utility for handle multiply git projects",
    entry_points={"console_scripts": ["gitlab_bulkcheckout=gitlab_bulkcheckout.cli:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="gitlab_bulkcheckout",
    name="gitlab_bulkcheckout",
    packages=find_packages(include=["gitlab_bulkcheckout"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nolte/gitlab_bulkcheckout",
    version="0.21.0",
    zip_safe=False,
)
