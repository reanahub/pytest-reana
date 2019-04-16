Changes
=======

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
