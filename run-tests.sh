# -*- coding: utf-8 -*-
#
# This file is part of REANA-Pytest-Commons.
# Copyright (C) 2018 CERN.
#
# REANA-Pytest-Commons is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

pydocstyle reana_pytest_commons && \
isort -rc -c -df **/*.py && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
