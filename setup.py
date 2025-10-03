# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures for REANA."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open("README.md").read()
history = open("CHANGELOG.md").read()

extras_require = {
    "docs": [
        "myst-parser",
        "Sphinx>=1.5.1",
        "sphinx-rtd-theme>=0.1.9",
    ],
}

extras_require["all"] = []
for key, reqs in extras_require.items():
    if ":" == key[0]:
        continue
    extras_require["all"].extend(reqs)

install_requires = [
    # apispec>=4.0 drops support for marshmallow<3
    "apispec[yaml]>=3.0,<4.0",
    "apispec-webframeworks",
    "check-manifest>=0.25,<1",
    "checksumdir>=1.1.4,<1.2",
    "coverage>=5.0,<8.0",
    "jsonschema>=3.2.0,<4.0",
    "mock>=3.0,<4.0",
    "pika>=0.12.0,<0.13",
    "pydocstyle>=5.0.0,<6.0.0",
    "pytest-cache>=1.0,<2.0",
    "pytest-cov>=3.0.0,<4.0",
    "pytest>=7.0.0,<9.0.0",
    "reana-commons[kubernetes]>=0.95.0a1,<0.96.0",
    "reana-db>=0.95.0a1,<0.96.0",
    "swagger_spec_validator>=2.1.0",
]
packages = find_packages()


# Get the version string. Cannot be done with import!
with open(os.path.join("pytest_reana", "version.py"), "rt") as f:
    version = re.search(r'__version__\s*=\s*"(?P<version>.*)"\n', f.read()).group(
        "version"
    )

setup(
    name="pytest-reana",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="REANA",
    author_email="info@reana.io",
    url="https://github.com/reanahub/pytest-reana",
    packages=[
        "pytest_reana",
    ],
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "pytest11": [
            "reana = pytest_reana.plugin",
        ]
    },
)
