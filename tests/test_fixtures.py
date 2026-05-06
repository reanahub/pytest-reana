# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2020, 2021, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA pytest fixture and deprecation-shim tests."""

from __future__ import absolute_import, print_function

import importlib
import warnings


def test_tmp_shared_volume_path_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_sth(tmp_shared_volume_path):
            import os
            os.path.exists(tmp_shared_volume_path)
    """)

    # run pytest with the following cmd args
    testdir.runpytest()
    testdir.runpytest().assert_outcomes(passed=1)


def test_legacy_fixture_imports_resolve_to_new_homes():
    """``pytest_reana.fixtures`` shim re-exports the relocated fixtures."""
    from pytest_reana.fixtures import (
        serial_workflow,
        tmp_shared_volume_path,
        user0,
    )
    from pytest_reana.test_utils import make_mock_api_client

    from reana_commons.testing import (
        make_mock_api_client as new_make_mock_api_client,
        serial_workflow as new_serial_workflow,
        tmp_shared_volume_path as new_tmp_shared_volume_path,
    )
    from reana_db.testing import user0 as new_user0

    assert tmp_shared_volume_path is new_tmp_shared_volume_path
    assert serial_workflow is new_serial_workflow
    assert user0 is new_user0
    assert make_mock_api_client is new_make_mock_api_client


def test_legacy_fixtures_module_emits_deprecation_warning():
    """Importing ``pytest_reana.fixtures`` emits a DeprecationWarning."""
    import pytest_reana.fixtures

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", DeprecationWarning)
        importlib.reload(pytest_reana.fixtures)

    assert any(
        issubclass(w.category, DeprecationWarning)
        and "pytest_reana.fixtures is deprecated" in str(w.message)
        for w in caught
    )


def test_legacy_test_utils_module_emits_deprecation_warning():
    """Importing ``pytest_reana.test_utils`` emits a DeprecationWarning."""
    import pytest_reana.test_utils

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", DeprecationWarning)
        importlib.reload(pytest_reana.test_utils)

    assert any(
        issubclass(w.category, DeprecationWarning)
        and "pytest_reana.test_utils is deprecated" in str(w.message)
        for w in caught
    )


def test_legacy_plugin_path_still_wires_fixtures(testdir):
    """``pytest_plugins = ['pytest_reana.plugin']`` still resolves fixtures.

    The new ``reana_commons`` and ``reana_db`` pytest11 entry points are
    explicitly disabled in the sub-pytest run so that the only path for
    fixture discovery is the legacy ``pytest_reana.plugin`` shim.
    """
    testdir.makeconftest("""
        pytest_plugins = ["pytest_reana.plugin"]
    """)
    testdir.makepyfile("""
        def test_uses_legacy_plugin(serial_workflow, tmp_shared_volume_path):
            assert serial_workflow["reana_specification"]["workflow"]["type"] == "serial"
            assert tmp_shared_volume_path is not None
    """)
    result = testdir.runpytest("-p", "no:reana_commons", "-p", "no:reana_db")
    result.assert_outcomes(passed=1)
