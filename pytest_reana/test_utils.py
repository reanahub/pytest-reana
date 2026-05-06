# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2020, 2021, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Deprecated re-export of :func:`make_mock_api_client`.

The helper now lives in :mod:`reana_commons.testing`. Importing it from
``pytest_reana.test_utils`` still works but is deprecated and will be
removed in a future release.
"""

from __future__ import absolute_import, print_function

import warnings

from reana_commons.testing import make_mock_api_client  # noqa: F401

warnings.warn(
    "pytest_reana.test_utils is deprecated; import make_mock_api_client "
    "from reana_commons.testing instead.",
    DeprecationWarning,
    stacklevel=2,
)
