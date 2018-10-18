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
from kombu import Connection, Exchange, Producer, Queue
from mock import ANY, patch
from reana_commons.consumer import BaseConsumer
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
    """Return CWL workflow with name."""
    return {
        "reana_specification": {
            "parameters": {"min_year": "1991", "max_year": "2001"},
            "workflow": {
                "spec": {
                    "first": "do this",
                    "second": "do that"
                },
                "type": "cwl",
            },
            "specification": {},
            "type": "cwl",
        },
        "workflow_name": "my_test_workflow",
    }


@pytest.fixture()
def yadage_workflow_with_name():
    """Return yadage workflow with name."""
    return {
        "reana_specification": {
            "workflow": {
                "spec": {
                    "first": "do this",
                    "second": "do that"
                },
                "type": "yadage",
            },
            "parameters": {"min_year": "1991", "max_year": "2001"},
            "specification": {"first": "do this", "second": "do that"},
            "type": "yadage",
        },
        "name": "my_test_workflow",
    }


@pytest.fixture()
def cwl_workflow_without_name():
    """Return CWL workflow without name."""
    return {
        "reana_specification": {
            "parameters": {"min_year": "1991", "max_year": "2001"},
            "workflow": {
                "spec": {
                    "first": "do this",
                    "second": "do that"
                },
                "type": "cwl",
            },
            "specification": {},
            "type": "cwl",
        },
        "name": "",
    }


@pytest.fixture()
def yadage_workflow_without_name():
    """Return yadage workflow without name."""
    return {
        "reana_specification": {
            "workflow": {
                "spec": {
                    "first": "do this",
                    "second": "do that"
                },
                "type": "yadage",
            },
            "parameters": {"min_year": "1991", "max_year": "2001"},
            "specification": {"first": "do this", "second": "do that"},
            "type": "yadage",
        },
        "name": "",
    }


class _BaseConsumerTestIMPL(BaseConsumer):
    """Test implementation of a REANAConsumer class."""

    def get_consumers(self, Consumer, channel):
        """Sample get consumers method."""
        return [Consumer(queues=self.queues, callbacks=[self.on_message],
                         accept=[self.message_default_format])]

    def on_message(self, body, message):
        """Sample on message method."""
        message.ack()


@pytest.fixture
def ConsumerBase():
    """Return a class implementing a BaseConsumer."""
    return _BaseConsumerTestIMPL


@pytest.fixture
def ConsumerBaseOnMessageMock(ConsumerBase):
    """Return a BaseConsumer class with ``on_message`` mocked."""
    with patch.object(ConsumerBase, 'on_message'):
        yield ConsumerBase


@pytest.fixture
def consume_queue():
    """Provide a callable to consume a queue."""
    def _consume_queue(consumer, limit=None):
        """Consume AMQP queue.

        :param consumer: A :class:`kombu.Consumer` to consume from.
        :param limit: Integer which represents how many items to consume
            from the queue, if not specified, the consume method will run
            uninterruptedly.
        """
        consumer_generator = consumer.consume(limit=limit)
        while True:
            try:
                next(consumer_generator)
            except StopIteration:
                # no more items to consume in the queue
                break

    return _consume_queue


@pytest.fixture(scope='session')
def in_memory_queue_connection():
    """In memory message queue."""
    return Connection('memory:///')


@pytest.fixture
def default_exchange():
    """Return a default :class:`kombu.Exchange` created from configuration."""
    return Exchange('test-exchange', type='direct')


@pytest.fixture
def default_queue(default_exchange):
    """Return a default :class:`kombu.Queue` created from configuration."""
    return Queue('test-queue', exchange=default_exchange,
                 routing_key='test-routing-key')


@pytest.fixture
def default_in_memory_producer(in_memory_queue_connection, default_exchange):
    """Rerturn a :class:`kombu.Producer` connected to in memory queue."""
    return in_memory_queue_connection.Producer(
        exchange=default_exchange,
        routing_key='test-routing-key',
        serializer='json')
