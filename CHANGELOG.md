# Changelog

## [0.95.0](https://github.com/reanahub/pytest-reana/compare/0.9.2...0.95.0) (2025-01-15)


### ⚠ BREAKING CHANGES

* **fixtures:** This commit replaces the default_user fixture with user1 and user2 fixtures. The default_user fixture is now deprecated and will be removed in the next release.
* **python:** drop support for Python 3.6 and 3.7

### Build

* **python:** add minimal `pyproject.toml` ([#133](https://github.com/reanahub/pytest-reana/issues/133)) ([0ad190c](https://github.com/reanahub/pytest-reana/commit/0ad190c027c3707ffed14321845c8aa19a6d0111))
* **python:** add support for Python 3.13 ([#136](https://github.com/reanahub/pytest-reana/issues/136)) ([7ce8c29](https://github.com/reanahub/pytest-reana/commit/7ce8c293c00807e07d61068bce33208f511544c5))
* **python:** drop support for Python 3.6 and 3.7 ([#130](https://github.com/reanahub/pytest-reana/issues/130)) ([5065be0](https://github.com/reanahub/pytest-reana/commit/5065be0ae2afe63861c0a112a56c836c8682fec0))
* **python:** remove deprecated `pytest-runner` ([#133](https://github.com/reanahub/pytest-reana/issues/133)) ([3b79770](https://github.com/reanahub/pytest-reana/commit/3b797703f8ababf7efe6a2c73cd50c2661e6a779))


### Features

* **fixtures:** add user1 and user2 fixtures ([#113](https://github.com/reanahub/pytest-reana/issues/113)) ([67421e9](https://github.com/reanahub/pytest-reana/commit/67421e9e50997c0d3b076e7b5d994cb325a928e5))
* **fixtures:** add workflows owned by user1 ([#113](https://github.com/reanahub/pytest-reana/issues/113)) ([e906ba3](https://github.com/reanahub/pytest-reana/commit/e906ba3866288231df6d62c3542e8ce916f0c2cd))


### Bug fixes

* **fixtures:** delete shares and jobs before deleting workflow ([#113](https://github.com/reanahub/pytest-reana/issues/113)) ([b087fc2](https://github.com/reanahub/pytest-reana/commit/b087fc2b1c92e441ef31354b0a7b0b096530958f))
* **fixtures:** encode all user secrets in base64 ([#131](https://github.com/reanahub/pytest-reana/issues/131)) ([d4a07cf](https://github.com/reanahub/pytest-reana/commit/d4a07cfb08e9f73a26538e787c5e2d4be48b06b7))


### Code refactoring

* **docs:** move from reST to Markdown ([#123](https://github.com/reanahub/pytest-reana/issues/123)) ([4710f11](https://github.com/reanahub/pytest-reana/commit/4710f1195557c5e1ae1a993084f26010e035f822))


### Continuous integration

* **actions:** pin setuptools 70 ([#135](https://github.com/reanahub/pytest-reana/issues/135)) ([2c1995f](https://github.com/reanahub/pytest-reana/commit/2c1995fc4a319a9d5003476101b1e5014e6babb3))
* **actions:** update GitHub actions due to Node 16 deprecation ([#129](https://github.com/reanahub/pytest-reana/issues/129)) ([8710f89](https://github.com/reanahub/pytest-reana/commit/8710f8923d00096205d228a8d71b86f161e66141))
* **actions:** upgrade to Ubuntu 24.04 and Python 3.12 ([#132](https://github.com/reanahub/pytest-reana/issues/132)) ([f42d8b1](https://github.com/reanahub/pytest-reana/commit/f42d8b16d274310682aa703860c43bd70b4a2c91))
* **commitlint:** addition of commit message linter ([#118](https://github.com/reanahub/pytest-reana/issues/118)) ([67259a6](https://github.com/reanahub/pytest-reana/commit/67259a6c33413c84b53528413b88556b9cd2fb5d))
* **commitlint:** allow release commit style ([#125](https://github.com/reanahub/pytest-reana/issues/125)) ([bfee7a4](https://github.com/reanahub/pytest-reana/commit/bfee7a43c22771a8c3a39df81307029d1c6975f1))
* **commitlint:** check for the presence of concrete PR number ([#122](https://github.com/reanahub/pytest-reana/issues/122)) ([7cb6926](https://github.com/reanahub/pytest-reana/commit/7cb69260b2b4bfbcdf1de02b64fbc180db67fb81))
* **commitlint:** improve checking of merge commits ([#132](https://github.com/reanahub/pytest-reana/issues/132)) ([9477298](https://github.com/reanahub/pytest-reana/commit/94772988a727936c5979730d577bfb60a25d4eb2))
* **pytest:** invoke `pytest` directly instead of `setup.py test` ([#133](https://github.com/reanahub/pytest-reana/issues/133)) ([34bbcdc](https://github.com/reanahub/pytest-reana/commit/34bbcdc56a06e11a901dd4adece0e0d46db0d61c))
* **release-please:** initial configuration ([#118](https://github.com/reanahub/pytest-reana/issues/118)) ([b87d9e9](https://github.com/reanahub/pytest-reana/commit/b87d9e973a35ae00bc76422fc39f444dea36a8ae))
* **shellcheck:** check all shell scripts recursively ([#121](https://github.com/reanahub/pytest-reana/issues/121)) ([4ba7548](https://github.com/reanahub/pytest-reana/commit/4ba754893b5b20981413c812464e8171d6eebe29))
* **shellcheck:** fix exit code propagation ([#122](https://github.com/reanahub/pytest-reana/issues/122)) ([fd232e6](https://github.com/reanahub/pytest-reana/commit/fd232e6f1da0cd714755629376b8f0947597a387))
* **tox:** fix collecting code coverage information ([#134](https://github.com/reanahub/pytest-reana/issues/134)) ([023adcf](https://github.com/reanahub/pytest-reana/commit/023adcfef060f4599abd633bb3ee962e134a97ff))


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
