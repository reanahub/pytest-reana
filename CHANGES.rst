Changes
=======

Version 0.9.2 (2023-11-30)
--------------------------

- Changes CI to use the stable release of Python 3.12.

Version 0.9.1 (2023-09-26)
--------------------------

- Adds support for Python 3.12.
- Changes ``apispec`` dependency version in order to be compatible with ``PyYAML`` v6.
- Fixes container image fixtures to be Podman-compatible.
- Fixes Kombu documentation linking.

Version 0.9.0 (2022-12-13)
--------------------------

- Adds fixture providing example of user secrets needed for Kerberos tests.
- Adds support for Python 3.11.
- Fixes location of Celery docs for ReadTheDocs pages.
- Removes hard-dependency on `black` code formatter version.

Version 0.8.1 (2022-01-05)
--------------------------

- Adds support for Python 3.10.

Version 0.8.0 (2021-11-22)
---------------------------

- Adds nested Yadage workflow specification fixture.
- Adds empty workflow workspaces for sample workflows by default.
- Adds internal representation of a scatter-gather Snakemake workflow fixture.
- Changes ``tmp_shared_volume_path`` fixture to be configurable through environment variable.
- Changes fixtures to run with the full workspace path stored in the database.
- Removes support for Python 2.

Version 0.7.2 (2021-07-02)
--------------------------

- Changes internal dependencies to remove click.

Version 0.7.1 (2021-03-17)
--------------------------

- Adds support for Python 3.9.
- Fixes minor code warnings.
- Fixes installation by upgrading REANA-DB version.

Version 0.7.0 (2020-10-20)
--------------------------

- Adds new ``__reana`` database schema for ``db`` fixture.
- Fixes a problem related to duplicated database session.
- Changes code formatting to respect ``black`` coding style.
- Changes documentation to single-page layout.

Version 0.6.0 (2019-12-19)
--------------------------

- Adds fixtures for secrets store.
- Centralises test requirements.
- Adds Python 3.8 support.

Version 0.5.0 (2019-04-16)
--------------------------

- Makes workspace path configurable for the ``sample_workflow_workspace``
  fixture through the ``path`` parameter.
- Adds ``sample_serial_workflow_in_db`` fixture.
- Exposes previously hidden ``sample_yadage_workflow_in_db`` fixture.
- Adds missing database session close in ``session`` fixture.
- Adds helpers to represent starting and requeueing job conditions,
  ``sample_condition_for_starting_queued_workflows`` and
  ``sample_condition_for_requeueing_workflows``.

Version 0.4.1 (2018-11-06)
--------------------------

- Adds directory including sample workspace data.

Version 0.4.0 (2018-11-06)
--------------------------

- Initial public release.

.. admonition:: Please beware

   Please note that REANA is in an early alpha stage of its development. The
   developer preview releases are meant for early adopters and testers. Please
   don't rely on released versions for any production purposes yet.
