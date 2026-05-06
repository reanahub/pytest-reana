# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2019, 2020, 2021, 2022, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Deprecated pytest plugin for REANA.

This module is no longer registered as a ``pytest11`` plugin. The fixtures
it used to expose are now provided by ``reana_commons.testing.plugin`` and
``reana_db.testing.plugin``, which are auto-loaded via their own pytest
entry points when ``reana-commons[tests]`` or ``reana-db[tests]`` is
installed.

The module is kept as an importable shim so that legacy code that does
``from pytest_reana.plugin import ...`` still resolves.
"""

from __future__ import absolute_import, print_function

from .fixtures import *  # noqa: F401,F403
