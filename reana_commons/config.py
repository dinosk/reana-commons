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

"""REANA Commons flask configuration."""

import os


SQLALCHEMY_DATABASE_URI = \
    os.getenv('REANA_SQLALCHEMY_DATABASE_URI',
              'postgresql+psycopg2://reana:reana@'
              'dinosmbp.dyndns.cern.ch:5432/reana')

# BROKER = os.getenv("RABBIT_MQ", 'amqp://test:1234@'
#                    'message-broker.default.svc.cluster.local//')

# SHARED_VOLUME_PATH = os.getenv('SHARED_VOLUME_PATH', '/reana')
# """Path to the mounted REANA shared volume."""

# SQLALCHEMY_DATABASE_URI_TEMPLATE = 'sqlite:///{path}'.format(
#     path=os.path.join(SHARED_VOLUME_PATH, 'default/reana.db'))
# """SQLAlchemy database location"""

# ORGANIZATIONS = os.getenv('ORGANIZATIONS').split(',') \
#     if os.getenv('ORGANIZATIONS') else []
# """Organizations."""

# SQLALCHEMY_TRACK_MODIFICATIONS = False
# """Track modifications flag."""
