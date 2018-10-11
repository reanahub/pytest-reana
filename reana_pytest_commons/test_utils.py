# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.
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
