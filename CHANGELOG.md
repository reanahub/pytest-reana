# Changelog

## [0.95.0](https://github.com/reanahub/pytest-reana/compare/0.9.2...0.95.0) (2024-03-18)


### Code refactoring

* **docs:** move from reST to Markdown ([#123](https://github.com/reanahub/pytest-reana/issues/123)) ([4710f11](https://github.com/reanahub/pytest-reana/commit/4710f1195557c5e1ae1a993084f26010e035f822))


### Continuous integration

* **actions:** update GitHub actions due to Node 16 deprecation ([#129](https://github.com/reanahub/pytest-reana/issues/129)) ([8710f89](https://github.com/reanahub/pytest-reana/commit/8710f8923d00096205d228a8d71b86f161e66141))
* **commitlint:** addition of commit message linter ([#118](https://github.com/reanahub/pytest-reana/issues/118)) ([67259a6](https://github.com/reanahub/pytest-reana/commit/67259a6c33413c84b53528413b88556b9cd2fb5d))
* **commitlint:** allow release commit style ([#125](https://github.com/reanahub/pytest-reana/issues/125)) ([bfee7a4](https://github.com/reanahub/pytest-reana/commit/bfee7a43c22771a8c3a39df81307029d1c6975f1))
* **commitlint:** check for the presence of concrete PR number ([#122](https://github.com/reanahub/pytest-reana/issues/122)) ([7cb6926](https://github.com/reanahub/pytest-reana/commit/7cb69260b2b4bfbcdf1de02b64fbc180db67fb81))
* **release-please:** initial configuration ([#118](https://github.com/reanahub/pytest-reana/issues/118)) ([b87d9e9](https://github.com/reanahub/pytest-reana/commit/b87d9e973a35ae00bc76422fc39f444dea36a8ae))
* **shellcheck:** check all shell scripts recursively ([#121](https://github.com/reanahub/pytest-reana/issues/121)) ([4ba7548](https://github.com/reanahub/pytest-reana/commit/4ba754893b5b20981413c812464e8171d6eebe29))
* **shellcheck:** fix exit code propagation ([#122](https://github.com/reanahub/pytest-reana/issues/122)) ([fd232e6](https://github.com/reanahub/pytest-reana/commit/fd232e6f1da0cd714755629376b8f0947597a387))


### Documentation

* **authors:** complete list of contributors ([#124](https://github.com/reanahub/pytest-reana/issues/124)) ([39c0238](https://github.com/reanahub/pytest-reana/commit/39c0238b453c570e7d451669a53c63c7cf351650))


### Chores

* **master:** release 0.95.0a1 ([408888f](https://github.com/reanahub/pytest-reana/commit/408888f301e9f2514c284f79ab3e342be93ec2db))

## 0.9.2 (2023-11-30)

- Changes CI to use the stable release of Python 3.12.

## 0.9.1 (2023-09-26)

- Adds support for Python 3.12.
- Changes `apispec` dependency version in order to be compatible with `PyYAML` v6.
- Fixes container image fixtures to be Podman-compatible.
- Fixes Kombu documentation linking.

## 0.9.0 (2022-12-13)

- Adds fixture providing example of user secrets needed for Kerberos tests.
- Adds support for Python 3.11.
- Fixes location of Celery docs for ReadTheDocs pages.
- Removes hard-dependency on `black` code formatter version.

## 0.8.1 (2022-01-05)

- Adds support for Python 3.10.

## 0.8.0 (2021-11-22)

- Adds nested Yadage workflow specification fixture.
- Adds empty workflow workspaces for sample workflows by default.
- Adds internal representation of a scatter-gather Snakemake workflow fixture.
- Changes `tmp_shared_volume_path` fixture to be configurable through environment variable.
- Changes fixtures to run with the full workspace path stored in the database.
- Removes support for Python 2.

## 0.7.2 (2021-07-02)

- Changes internal dependencies to remove click.

## 0.7.1 (2021-03-17)

- Adds support for Python 3.9.
- Fixes minor code warnings.
- Fixes installation by upgrading REANA-DB version.

## 0.7.0 (2020-10-20)

- Adds new `__reana` database schema for `db` fixture.
- Fixes a problem related to duplicated database session.
- Changes code formatting to respect `black` coding style.
- Changes documentation to single-page layout.

## 0.6.0 (2019-12-19)

- Adds fixtures for secrets store.
- Centralises test requirements.
- Adds Python 3.8 support.

## 0.5.0 (2019-04-16)

- Makes workspace path configurable for the `sample_workflow_workspace`
  fixture through the `path` parameter.
- Adds `sample_serial_workflow_in_db` fixture.
- Exposes previously hidden `sample_yadage_workflow_in_db` fixture.
- Adds missing database session close in `session` fixture.
- Adds helpers to represent starting and requeueing job conditions,
  `sample_condition_for_starting_queued_workflows` and
  `sample_condition_for_requeueing_workflows`.

## 0.4.1 (2018-11-06)

- Adds directory including sample workspace data.

## 0.4.0 (2018-11-06)

- Initial public release.
