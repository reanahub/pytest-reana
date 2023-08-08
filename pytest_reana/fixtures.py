# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2019, 2020, 2021, 2022, 2023 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures for REANA."""

from __future__ import absolute_import, print_function

import base64
import json
import os
import shutil
from uuid import uuid4

import pkg_resources
import pytest
from kombu import Connection, Exchange, Queue
from kubernetes import client
from mock import Mock, patch
from reana_commons.consumer import BaseConsumer
from reana_db.utils import build_workspace_path
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import create_database, database_exists


@pytest.yield_fixture(scope="module")
def tmp_shared_volume_path(tmpdir_factory):
    """Fixture temporary file system database.

    Scope: module

    This fixture offers a temporary shared file system using
    ``tmpdir_factory.mktemp`` named ``reana`` and when scoped is finished
    it will be deleted.

    .. code-block:: python

        import os

        def test_dir_exists(tmp_shared_volume_path):
            path = os.path.join(
                tmp_shared_volume_path, 'directory_path')
            assert os.path.exists(path)

    """
    shared_volume_path = os.getenv("SHARED_VOLUME_PATH", "")
    temp_path = None
    if not os.path.exists(shared_volume_path):
        temp_path = str(tmpdir_factory.mktemp("reana"))
    yield temp_path or shared_volume_path
    if temp_path:
        shutil.rmtree(temp_path)


@pytest.fixture()
def session():
    """Create a SQL Alchemy session.

    Scope: function

    This fixture offers a SQLAlchemy session which has been created from the
    ``db_engine`` fixture.

    .. code-block:: python

        from reana_db.models import Workflow

        def test_create_workflow(session):
            workflow = Workflow(...)
            session.add(workflow)
            session.commit()
    """
    from reana_db.database import Session

    yield Session
    Session.close()


@pytest.fixture()
def app(base_app):
    """Flask application fixture.

    Scope: function

    This fixture offers a Flask application with already a database connection
    and all the models created. When finished it will delete all models.

    .. code-block:: python

        def create_ninja_turtle()
            with app.test_client() as client:
                somedata = 'ninja turtle'
                res = client.post(url_for('api.create_object'),
                                  content_type='application/json',
                                  data=json.dumps(somedata))

                assert res.status_code == 200

    """
    from reana_db.database import Session
    from reana_db.models import Base, Resource

    engine = create_engine(base_app.config["SQLALCHEMY_DATABASE_URI"])
    base_app.session.bind = engine
    with base_app.app_context():
        if not engine.dialect.has_schema(engine, "__reana"):
            engine.execute(CreateSchema("__reana"))
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(bind=engine)
        Resource.initialise_default_resources()
        yield base_app
        Session.close()  # close hanging connections
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def default_user(app, session):
    """Create users.

    Scope: function

    This fixture creates an user with a default UUID
    ``00000000-0000-0000-0000-000000000000``, ``email`` `info@reana.io`
    and ``access_token`` ``secretkey`` and returns it.

    .. code-block:: python

        def test_default_user_exists(default)
            with app.test_client() as client:
                res = client.post(url_for('api.get_users'),
                                  query_string={"user": default_user.id_})

                assert res.status_code == 200


    """
    from reana_db.models import User

    default_user_id = "00000000-0000-0000-0000-000000000000"
    user = User.query.filter_by(id_=default_user_id).first()
    if not user:
        with patch("reana_db.database.Session", return_value=session):
            user = User(
                id_=default_user_id, email="info@reana.io", access_token="secretkey"
            )
        session.add(user)
        session.commit()
    return user


@pytest.fixture()
def serial_workflow():
    """Create a serial workflow.

    Scope: function

    This fixture provides a ``serial`` workflow.
    """
    return {
        "reana_specification": {
            "workflow": {
                "specification": {
                    "steps": [
                        {
                            "environment": "docker.io/reanahub/reana-env-jupyter",
                            "commands": ["echo 'Hello REANA'"],
                        }
                    ]
                },
                "type": "serial",
            },
        },
    }


@pytest.fixture()
def cwl_workflow_with_name():
    """CWL workflow with name.

    Scope: function

    This fixture provides a ``CWL`` workflow with a name as a dictionary.
    """
    return {
        "reana_specification": {
            "inputs": {"parameters": {"min_year": "1991", "max_year": "2001"}},
            "workflow": {
                "specification": {"first": "do this", "second": "do that"},
                "type": "cwl",
            },
            "type": "cwl",
        },
        "workflow_name": "my_test_workflow",
    }


@pytest.fixture()
def yadage_workflow_with_name():
    """Yadage workflow with name.

    Scope: function

    This fixture provides a ``yadage`` workflow with a name as a dictionary.
    """
    return {
        "reana_specification": {
            "workflow": {
                "specification": {"first": "do this", "second": "do that"},
                "type": "yadage",
            },
            "inputs": {"parameters": {"min_year": "1991", "max_year": "2001"}},
            "type": "yadage",
        },
        "name": "my_test_workflow",
    }


@pytest.fixture()
def cwl_workflow_without_name():
    """CWL workflow without name.

    Scope: function

    This fixture provides a ``CWL`` workflow without a name as a dictionary.
    """
    return {
        "reana_specification": {
            "inputs": {"parameters": {"min_year": "1991", "max_year": "2001"}},
            "workflow": {
                "specification": {"first": "do this", "second": "do that"},
                "type": "cwl",
            },
            "type": "cwl",
        },
        "name": "",
    }


@pytest.fixture()
def yadage_workflow_without_name():
    """Yadage workflow without name.

    Scope: function

    This fixture provides a ``yadage`` workflow without name as a dictionary.
    """
    return {
        "reana_specification": {
            "workflow": {
                "specification": {"first": "do this", "second": "do that"},
                "type": "yadage",
            },
            "inputs": {"parameters": {"min_year": "1991", "max_year": "2001"}},
            "type": "yadage",
        },
        "name": "",
    }


@pytest.fixture()
def yadage_workflow_spec_loaded():
    """Nested Yadage workflow.

    Scope: function

    This fixture provides a nested ``yadage`` workflow spec loaded as dictionary.
    """
    return {
        "version": "0.7.2",
        "inputs": {
            "files": ["code/foo.C", "code/bar.C"],
            "directories": ["workflow/yadage"],
            "parameters": {"foo": "foo_val", "bar": "bar_val", "baz": "baz_val"},
        },
        "outputs": {"files": ["fitdata/plot.png"]},
        "workflow": {
            "type": "yadage",
            "file": "workflow/yadage/workflow.yaml",
            "specification": {
                "stages": [
                    {
                        "name": "gendata",
                        "dependencies": {
                            "dependency_type": "jsonpath_ready",
                            "expressions": ["init"],
                        },
                        "scheduler": {
                            "scheduler_type": "singlestep-stage",
                            "parameters": [
                                {
                                    "key": "foo",
                                    "value": {
                                        "step": "init",
                                        "output": "foo",
                                        "expression_type": "stage-output-selector",
                                    },
                                },
                                {
                                    "key": "bar",
                                    "value": {
                                        "step": "init",
                                        "output": "bar",
                                        "expression_type": "stage-output-selector",
                                    },
                                },
                            ],
                            "step": {
                                "process": {
                                    "process_type": "interpolated-script-cmd",
                                    "script": "python --foo '{foo}/{bar}'",
                                    "interpreter": "sh",
                                },
                                "publisher": {
                                    "publisher_type": "frompar-pub",
                                    "outputmap": {"data": "outfilename"},
                                },
                                "environment": {
                                    "environment_type": "docker-encapsulated",
                                    "image": "docker.io/reanahub/reana-env-root6",
                                    "imagetag": "6.18.04",
                                    "resources": [],
                                    "envscript": "",
                                    "env": {},
                                    "workdir": None,
                                    "par_mounts": [],
                                },
                            },
                        },
                    },
                    {
                        "name": "fitdata",
                        "dependencies": {
                            "dependency_type": "jsonpath_ready",
                            "expressions": ["gendata"],
                        },
                        "scheduler": {
                            "scheduler_type": "singlestep-stage",
                            "parameters": [
                                {
                                    "key": "baz",
                                    "value": {
                                        "step": "init",
                                        "output": "baz",
                                        "expression_type": "stage-output-selector",
                                    },
                                },
                                {
                                    "key": "bar",
                                    "value": {
                                        "step": "gendata",
                                        "output": "bar",
                                        "expression_type": "stage-output-selector",
                                    },
                                },
                            ],
                            "step": {
                                "process": {
                                    "process_type": "interpolated-script-cmd",
                                    "script": 'root -b -q \'("{baz}","{bar}")\'',
                                    "interpreter": "sh",
                                },
                                "publisher": {
                                    "publisher_type": "frompar-pub",
                                    "outputmap": {"plot": "outfile"},
                                },
                                "environment": {
                                    "environment_type": "docker-encapsulated",
                                    "image": "docker.io/reanahub/reana-env-root6",
                                    "imagetag": "6.18.04",
                                    "resources": [],
                                    "envscript": "",
                                    "env": {},
                                    "workdir": None,
                                    "par_mounts": [],
                                },
                            },
                        },
                    },
                    {
                        "name": "parent_step",
                        "dependencies": {
                            "dependency_type": "jsonpath_ready",
                            "expressions": [""],
                        },
                        "scheduler": {
                            "scheduler_type": "singlestep-stage",
                            "parameters": [
                                {
                                    "key": "nested_foo",
                                    "value": {
                                        "step": "init",
                                        "output": "nested_foo",
                                        "expression_type": "stage-output-selector",
                                    },
                                },
                            ],
                            "workflow": {
                                "stages": [
                                    {
                                        "name": "nested_step",
                                        "dependencies": {
                                            "dependency_type": "jsonpath_ready",
                                            "expressions": ["run_mc"],
                                        },
                                        "scheduler": {
                                            "scheduler_type": "singlestep-stage",
                                            "parameters": [
                                                {
                                                    "key": "nested_foo",
                                                    "value": {
                                                        "step": "init",
                                                        "output": "nested_foo",
                                                    },
                                                },
                                                {
                                                    "key": "inputs",
                                                    "value": {
                                                        "stages": "run_mc[*].mergeallvars",
                                                        "output": "mergedfile",
                                                        "expression_type": "stage-output-selector",
                                                    },
                                                },
                                                {
                                                    "key": "mergedfile",
                                                    "value": "{workdir}/merged.root",
                                                },
                                            ],
                                            "step": {
                                                "process": {
                                                    "process_type": "interpolated-script-cmd",
                                                    "interpreter": "bash",
                                                    "script": "source /usr/local/bin/{nested_foo}.sh\nhadd {mergedfile} {inputs}\n",
                                                },
                                                "environment": {
                                                    "environment_type": "docker-encapsulated",
                                                    "image": "docker.io/reanahub/reana-env-root6",
                                                    "imagetag": "6.18.04",
                                                    "resources": [],
                                                    "envscript": "",
                                                    "env": {},
                                                    "workdir": None,
                                                    "par_mounts": [],
                                                },
                                                "publisher": {
                                                    "publisher_type": "frompar-pub",
                                                    "outputmap": {
                                                        "mergedfile": "mergedfile"
                                                    },
                                                },
                                            },
                                        },
                                    }
                                ]
                            },
                        },
                    },
                ]
            },
        },
    }


@pytest.fixture()
def snakemake_workflow_spec_loaded():
    """Scatter-gather Snakemake workflow.

    Scope: function

    This fixture provides the internal representation of a basic scatter-gather ``snakemake`` workflow loaded as dictionary.
    """
    return {
        "version": "0.8.0",
        "workflow": {
            "type": "snakemake",
            "file": "workflow/snakemake/Snakemake",
            "specification": {
                "job_dependencies": {
                    "all": ["gather"],
                    "gather": ["scatterA", "scatterB"],
                    "scatterA": [],
                    "scatterB": [],
                },
                "steps": [
                    {
                        "commands": ["sleep 15 && mkdir -p results && touch {output}"],
                        "environment": "python:2.7-slim",
                        "inputs": {},
                        "kubernetes_memory_limit": None,
                        "kubernetes_uid": None,
                        "name": "scatterA",
                        "outputs": {},
                        "params": {},
                    },
                    {
                        "commands": ["sleep 30 && mkdir -p results && touch {output}"],
                        "environment": "python:2.7-slim",
                        "inputs": {},
                        "kubernetes_memory_limit": None,
                        "kubernetes_uid": None,
                        "name": "scatterB",
                        "outputs": {},
                        "params": {},
                    },
                    {
                        "commands": ["sleep 5 && touch {output}"],
                        "environment": "python:2.7-slim",
                        "inputs": {},
                        "kubernetes_memory_limit": None,
                        "kubernetes_uid": None,
                        "name": "gather",
                        "outputs": {},
                        "params": {},
                    },
                ],
            },
        },
    }


class _BaseConsumerTestIMPL(BaseConsumer):
    """Test implementation of a REANAConsumer class.

    This class is a basic implementation of a ``reana_commons.BaseConsumer``
    to use while testing. There are fixtures wrapping it so it shouldn't
    be used directly.
    """

    def get_consumers(self, Consumer, channel):
        """Sample get consumers method."""
        return [
            Consumer(
                self.queue,
                callbacks=[self.on_message],
                accept=[self.message_default_format],
            )
        ]

    def on_message(self, body, message):
        """Sample on message method."""
        message.ack()


@pytest.fixture
def ConsumerBase():
    """Return a class implementing a BaseConsumer.

    Scope: function

    This fixture offers a class which implements the
    ``reana_commons.BaseConsumer``. It will just acknowledge the received
    messages.
    """
    return _BaseConsumerTestIMPL


@pytest.fixture
def ConsumerBaseOnMessageMock(ConsumerBase):
    """Return a BaseConsumer class with ``on_message`` mocked.

    Scope: function

    This fixture offers a class which implements the
    ``reana_commons.BaseConsumer``. Additionally to the ``ConsumerBase``
    fixture, this class has an ``on_message`` mocked method so actions like
    the following can be performed.

    .. code-block:: python

        def test_msg(ConsumerBaseOnMessageMock)
            consumer = ConsumerBaseOnMessageMock()
            # 1 message is published with message {'some': 'message'}
            expected_body = {'some': 'message'}
            consumer.on_message.assert_called_once_with(
                expected, ANY)

    """
    with patch.object(ConsumerBase, "on_message"):
        yield ConsumerBase


@pytest.fixture
def consume_queue():
    """Provide a callable to consume a queue.

    Scope: function

    This fixture offers a function which given a ``kombu.Consumer`` will
    consume the messages in the queue until a certain ``limit``. If ``limit``
    is not specified it will consume uninterruptedly.

    .. code-block:: python

        def test_consume_1_msg(ConsumerBase, consume_queue)
            consumer = ConsumerBase()
            # some message is published in the queue
            # and we want to consume only one.
            consume_queue(consumer, limit=1)

    """

    def _consume_queue(consumer, limit=None):
        """Consume AMQP queue.

        :param consumer: A class:`kombu.Consumer` to consume from.
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


@pytest.fixture(scope="session")
def in_memory_queue_connection():
    """In memory message queue.

    Scope: session

    This fixture offers an in memory class:`kombu.Connection` scoped to the
    testing session.

    .. code-block:: python

        def test_something(ConsumerBase, in_memory_queue_connection):
            consumer = ConsumerBase(connection=in_memory_queue_connection)
            # Now you have a consumer connected to an in memory queue


    """
    return Connection("memory:///")


@pytest.fixture
def default_exchange():
    """Return a default class:`kombu.Exchange` created from configuration.

    Scope: function

    This fixture offers a default class:`kombu.Exchange`.
    """
    return Exchange("test-exchange", type="direct")


@pytest.fixture
def default_queue(default_exchange):
    """Return a default class:`kombu.Queue` created from configuration.

    Scope: function

    This fixture offers a default class:`kombu.Queue`.
    """
    return Queue(
        "test-queue", exchange=default_exchange, routing_key="test-routing-key"
    )


@pytest.fixture
def default_in_memory_producer(in_memory_queue_connection, default_exchange):
    """Rerturn a class:`kombu.Producer` connected to in memory queue.

    Scope: function

    This fixture offers a default class:`kombu.Producer` instantiated using
    the ``in_memory_queue_connection``.

    .. code-block:: python

        def test_publish_hello(default_in_memory_producer, default_queue):
            msg = {'hello': 'ninja turtle'}
            default_in_memory_producer.publish(msg,
                                               declare=[default_queue])

    """
    return in_memory_queue_connection.Producer(
        exchange=default_exchange, routing_key="test-routing-key", serializer="json"
    )


@pytest.fixture(scope="module")
def sample_workflow_workspace(tmp_shared_volume_path):
    """Return the directory path of a sample workspace.

    Scope: module

    Creates a sample workspace in the shared volume path. Copies contents from
    the ``tests/test_workspace`` directory.

    """

    def _create_sample_workflow_workspace(relative_workspace_path):
        empty_workspace = os.path.join(tmp_shared_volume_path, relative_workspace_path)
        if not os.path.exists(empty_workspace):
            os.makedirs(empty_workspace)
        yield empty_workspace

    return _create_sample_workflow_workspace


@pytest.fixture()
def sample_yadage_workflow_in_db(
    app,
    default_user,
    session,
    yadage_workflow_with_name,
    sample_workflow_workspace,
    tmp_shared_volume_path,
):
    """Create a sample workflow in the database.

    Scope: function

    Adds a sample yadage workflow in the DB.
    """
    from reana_db.models import Workflow

    workflow_id = uuid4()
    relative_workspace_path = build_workspace_path(
        default_user.id_, workflow_id, tmp_shared_volume_path
    )
    next(sample_workflow_workspace(relative_workspace_path))
    workflow = Workflow(
        id_=workflow_id,
        name="sample_serial_workflow_1",
        owner_id=default_user.id_,
        reana_specification=yadage_workflow_with_name["reana_specification"],
        operational_options={},
        type_=yadage_workflow_with_name["reana_specification"]["workflow"]["type"],
        logs="",
        workspace_path=relative_workspace_path,
    )
    session.add(workflow)
    session.commit()
    yield workflow
    for resource in workflow.resources:
        session.delete(resource)
    session.delete(workflow)
    session.commit()


@pytest.fixture()
def sample_serial_workflow_in_db(
    app,
    default_user,
    session,
    serial_workflow,
    sample_workflow_workspace,
    tmp_shared_volume_path,
):
    """Create a sample workflow in the database.

    Scope: function

    Adds a sample serial workflow in the DB.
    """
    from reana_db.models import Workflow

    workflow_id = uuid4()
    relative_workspace_path = build_workspace_path(
        default_user.id_, workflow_id, tmp_shared_volume_path
    )
    next(sample_workflow_workspace(relative_workspace_path))
    workflow = Workflow(
        id_=workflow_id,
        name="sample_serial_workflow_1",
        owner_id=default_user.id_,
        reana_specification=serial_workflow["reana_specification"],
        operational_options={},
        type_=serial_workflow["reana_specification"]["workflow"]["type"],
        logs="",
        workspace_path=relative_workspace_path,
    )
    session.add(workflow)
    session.commit()
    yield workflow
    for resource in workflow.resources:
        session.delete(resource)
    session.delete(workflow)
    session.commit()


def sample_condition_for_starting_queued_workflows():
    """Sample always true condition."""
    return True


def sample_condition_for_requeueing_workflows():
    """Sample always false condition."""
    return False


@pytest.fixture
def no_db_user():
    """Mock user created without using db."""
    user = Mock()
    user.id_ = uuid4()
    return user


@pytest.fixture
def user_secrets():
    """Test user secrets dictionary."""
    keytab_file = base64.b64encode(b"keytab file.")
    user_secrets = {
        "username": {"value": "reanauser", "type": "env"},
        "password": {"value": "1232456", "type": "env"},
        ".keytab": {"value": keytab_file, "type": "file"},
    }
    return user_secrets


@pytest.fixture
def kerberos_user_secrets():
    """User secrets needed by Kerberos."""
    user_secrets = {
        "CERN_USER": {"value": b"johndoe", "type": "env"},
        "CERN_KEYTAB": {"value": b".keytab", "type": "env"},
        ".keytab": {"value": b"keytab file", "type": "file"},
    }
    for secret in user_secrets.values():
        secret["value"] = base64.b64encode(secret["value"])
    return user_secrets


@pytest.fixture
def empty_user_secrets():
    """Empty user secrets dictionary."""
    return {}


@pytest.fixture
def corev1_api_client_with_user_secrets(no_db_user):
    """Kubernetes CoreV1 api client with user secrets in K8s secret store.

    Scope: function

    Adds the CoreV1APIClient with example user secrets.
    """

    def make_corev1_api_client_with_user_secrets(user_secrets):
        """Callable to return.

        Should be used with one of the secret store fixtures.
        """
        corev1_api_client = Mock()
        metadata = client.V1ObjectMeta(name=str(no_db_user.id_))
        metadata.annotations = {"secrets_types": "{}"}
        user_secrets_values = {}
        secrets_types = {}
        for secret_name in user_secrets:
            # Add type metadata to secret store
            secrets_types[secret_name] = user_secrets[secret_name]["type"]
            user_secrets_values[secret_name] = user_secrets[secret_name]["value"]
        metadata.annotations["secrets_types"] = json.dumps(secrets_types)
        k8s_secrets_store = client.V1Secret(
            api_version="v1", metadata=metadata, data=user_secrets_values
        )
        corev1_api_client.read_namespaced_secret = (
            lambda name, namespace: k8s_secrets_store
        )
        return corev1_api_client

    return make_corev1_api_client_with_user_secrets
