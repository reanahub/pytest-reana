# pytest-REANA

[![image](https://img.shields.io/pypi/pyversions/pytest-reana.svg)](https://pypi.org/pypi/pytest-reana)
[![image](https://github.com/reanahub/pytest-reana/workflows/CI/badge.svg)](https://github.com/reanahub/pytest-reana/actions)
[![image](https://readthedocs.org/projects/pytest-reana/badge/?version=latest)](https://pytest-reana.readthedocs.io/en/latest/?badge=latest)
[![image](https://codecov.io/gh/reanahub/pytest-reana/branch/master/graph/badge.svg)](https://codecov.io/gh/reanahub/pytest-reana)
[![image](https://img.shields.io/badge/discourse-forum-blue.svg)](https://forum.reana.io)
[![image](https://img.shields.io/github/license/reanahub/pytest-reana.svg)](https://github.com/reanahub/pytest-reana/blob/master/LICENSE)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About

pytest-REANA is a component of the [REANA](http://www.reana.io/) reusable and
reproducible research data analysis platform. It provides pytest fixtures and
test utilities.

> **Deprecated.** Starting with this release, the fixtures and helpers
> previously shipped here live in the libraries that own them:
>
> - REANA-Commons-coupled and pure fixtures, plus `make_mock_api_client`, are
>   exported from `reana_commons.testing` and auto-loaded via
>   `reana-commons[tests]`.
> - Database-coupled fixtures are exported from `reana_db.testing` and
>   auto-loaded via `reana-db[tests]`.
>
> Existing imports from `pytest_reana.fixtures` and `pytest_reana.test_utils`
> continue to work but emit a `DeprecationWarning`. New projects should depend
> on `reana-commons[tests]` and/or `reana-db[tests]` instead of `pytest-reana`.
> The package will be archived once the deprecation cycle ends.

## Features

- pytest fixtures (now provided by `reana-commons[tests]` and `reana-db[tests]`)
- mocking OpenAPI client with request format validation
- mocking Advanced Message Queuing Protocol consumers and producers
- mocking Celery tasks
- mocking file system workspace access
- mocking database access

## Usage

The detailed information on how to install and use REANA can be found in
[docs.reana.io](https://docs.reana.io).

## Useful links

- [REANA project home page](http://www.reana.io/)
- [REANA user documentation](https://docs.reana.io)
- [REANA user support forum](https://forum.reana.io)
- [pytest-REANA releases](https://pytest-reana.readthedocs.io/en/latest#changes)
- [pytest-REANA developer documentation](https://pytest-reana.readthedocs.io/)
- [pytest-REANA known issues](https://github.com/reanahub/pytest-reana/issues)
- [pytest-REANA source code](https://github.com/reanahub/pytest-reana)
