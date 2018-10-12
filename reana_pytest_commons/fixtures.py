# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures for REANA."""

from __future__ import absolute_import, print_function

import os
import shutil

import pytest


@pytest.yield_fixture(scope='module')
def tmp_shared_volume_path(tmpdir_factory):
    """Fixture temporary file system database."""
    temp_path = str(tmpdir_factory.mktemp('reana'))
    yield temp_path
    shutil.rmtree(temp_path)
