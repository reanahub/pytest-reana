# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Deprecated re-exports of REANA pytest fixtures.

The fixtures previously living in this module now live in
:mod:`reana_commons.testing` (commons- and pure-helpers) and
:mod:`reana_db.testing` (database-coupled helpers). Importing from
``pytest_reana.fixtures`` still works but is deprecated and will be removed
in a future release.
"""

from __future__ import absolute_import, print_function

import warnings

from reana_commons.testing import (  # noqa: F401
    ConsumerBase,
    ConsumerBaseOnMessageMock,
    consume_queue,
    corev1_api_client_with_user_secrets,
    cwl_workflow_with_name,
    cwl_workflow_without_name,
    default_exchange,
    default_in_memory_producer,
    default_queue,
    empty_user_secrets,
    in_memory_queue_connection,
    kerberos_user_secrets,
    no_db_user,
    sample_workflow_workspace,
    serial_workflow,
    snakemake_workflow_spec_loaded,
    tmp_shared_volume_path,
    user_secrets,
    yadage_workflow_spec_loaded,
    yadage_workflow_with_name,
    yadage_workflow_without_name,
)
from reana_db.testing import (  # noqa: F401
    app,
    sample_condition_for_requeueing_workflows,
    sample_condition_for_starting_queued_workflows,
    sample_serial_workflow_in_db,
    sample_serial_workflow_in_db_owned_by_user1,
    sample_yadage_workflow_in_db,
    sample_yadage_workflow_in_db_owned_by_user1,
    session,
    user0,
    user1,
    user2,
)

warnings.warn(
    "pytest_reana.fixtures is deprecated; import fixtures from "
    "reana_commons.testing or reana_db.testing instead. Both libraries "
    "register pytest plugins automatically via the pytest11 entry point.",
    DeprecationWarning,
    stacklevel=2,
)
