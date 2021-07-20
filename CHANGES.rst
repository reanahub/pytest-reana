Changes
=======

Version 0.8.0 (UNRELEASED)
---------------------------

- Makes the `tmp_shared_volume_path` configurable through environment variable.
- Creates empty workflow workspaces for sample workflows by default.
- Adds nested Yadage workflow specification fixture.
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
