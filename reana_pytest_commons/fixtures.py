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
from reana_db.models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database


@pytest.yield_fixture(scope='module')
def tmp_shared_volume_path(tmpdir_factory):
    """Fixture temporary file system database."""
    temp_path = str(tmpdir_factory.mktemp('reana'))
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture(scope='module')
def db_engine(base_app):
    """Create a SQL Alchemy DB engine."""
    test_db_engine = create_engine(
        base_app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(test_db_engine.url):
        create_database(test_db_engine.url)
    yield test_db_engine
    drop_database(test_db_engine.url)


@pytest.fixture()
def session(db_engine):
    """Create a SQL Alchemy session."""
    Session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=db_engine))
    Base.query = Session.query_property()
    from reana_db.database import Session as _Session
    _Session.configure(bind=db_engine)
    yield Session


@pytest.fixture()
def app(base_app, db_engine, session):
    """Flask application fixture."""
    with base_app.app_context():
        import reana_db.models
        Base.metadata.create_all(bind=db_engine)
        yield base_app
        for table in reversed(Base.metadata.sorted_tables):
            db_engine.execute(table.delete())


@pytest.fixture()
def default_user(app, session):
    """Create users."""
    default_user_id = '00000000-0000-0000-0000-000000000000'
    user = User.query.filter_by(
        id_=default_user_id).first()
    if not user:
        user = User(id_=default_user_id,
                    email='info@reana.io', access_token='secretkey')
        session.add(user)
        session.commit()
    return user


@pytest.fixture()
def cwl_workflow_with_name():
    """CWL workflow with name."""
    return {'parameters': {'min_year': '1991',
                           'max_year': '2001'},
            'specification': {'first': 'do this',
                              'second': 'do that'},
            'type': 'cwl',
            'name': 'my_test_workflow'}


@pytest.fixture()
def yadage_workflow_with_name():
    """Yadage workflow with name."""
    return {'parameters': {'min_year': '1991',
                           'max_year': '2001'},
            'specification': {'first': 'do this',
                              'second': 'do that'},
            'type': 'yadage',
            'name': 'my_test_workflow'}


@pytest.fixture()
def cwl_workflow_without_name():
    """CWL workflow without name."""
    return {'parameters': {'min_year': '1991',
                           'max_year': '2001'},
            'specification': {'first': 'do this',
                              'second': 'do that'},
            'type': 'cwl',
            'name': ''}


@pytest.fixture()
def yadage_workflow_without_name():
    """Yadage workflow without name."""
    return {'parameters': {'min_year': '1991',
                           'max_year': '2001'},
            'specification': {'first': 'do this',
                              'second': 'do that'},
            'type': 'yadage',
            'name': ''}