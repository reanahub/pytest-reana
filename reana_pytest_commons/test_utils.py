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

"""Pytest fixtures for REANA."""

from __future__ import absolute_import, print_function

import pytest

from reana_commons.consumer import REANABaseConsumer


class REANABaseConsumerTestIMPL(REANABaseConsumer):
    """Test implementation of a REANAConsumer class."""

    def get_consumers(self, Consumer, channel):
        """Implement providing kombu.Consumers with queues/callbacks."""
        return [Consumer(queues=self.queues, callbacks=[self.on_message],
                         accept=[self.default_serializer])]

    def on_message(self, body, message):
        """Implement this method to manipulate the data received."""
        print(body)
        message.ack()
