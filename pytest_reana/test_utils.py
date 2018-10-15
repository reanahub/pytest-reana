# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
"""REANA Pytest Commons test utilities."""

import click
from mock import Mock
from reana_commons.api_client import BaseAPIClient


def make_mock_api_client(component):
    mock_http_client, mock_result, mock_response = Mock(), Mock(), Mock()
    mock_response.status_code = 200
    mock_result.result.return_value = ('_', mock_response)
    mock_http_client.request.return_value = mock_result
    mock_api_client = BaseAPIClient(component,
                                    http_client=mock_http_client)
    return mock_api_client._client
