=================
sqlalchemy-things
=================
|ReadTheDocs| |PyPI release| |PyPI downloads| |License| |Python versions| |GitHub CI| |Codecov|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/sqlalchemy-things/badge/?version=latest
  :target: https://sqlalchemy-things.readthedocs.io/en/latest/?badge=latest
  :alt: Read The Docs build

.. |PyPI release| image:: https://badge.fury.io/py/sqlalchemy-things.svg
  :target: https://pypi.org/project/sqlalchemy-things/
  :alt: Release

.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/sqlalchemy-things
  :target: https://pypistats.org/packages/sqlalchemy-things
  :alt: PyPI downloads count

.. |License| image:: https://img.shields.io/badge/License-MIT-green
  :target: https://github.com/ri-gilfanov/sqlalchemy-things/blob/master/LICENSE
  :alt: MIT License

.. |Python versions| image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue
  :target: https://pypi.org/project/sqlalchemy-things/
  :alt: Python version support

.. |GitHub CI| image:: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml/badge.svg?branch=master
  :target: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml
  :alt: GitHub continuous integration

.. |Codecov| image:: https://codecov.io/gh/ri-gilfanov/sqlalchemy-things/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/ri-gilfanov/sqlalchemy-things
  :alt: codecov.io status for master branch

Utility collection for development with `SQLAlchemy 1.4 / 2.0
<https://www.sqlalchemy.org/>`_ ORM.

Custom column types
-------------------
* column_types.UUIDType

Mixins for signle and joined inheritance
----------------------------------------
* declarative.InheritedPrimaryKeyMixin
* declarative.PolymorphicMixin

Primary key mixins for signle table inheritance
-----------------------------------------------
* declarative.BigIntegerPrimaryKeyMixin
* declarative.DateTimePrimaryKeyMixin
* declarative.IntegerPrimaryKeyMixin
* declarative.UUIDPrimaryKeyMixin

Primary key mixins for joined table inheritance
-----------------------------------------------
* declarative.CascadeBigIntegerPrimaryKeyMixin
* declarative.CascadeDateTimePrimaryKeyMixin
* declarative.CascadeIntegerPrimaryKeyMixin
* declarative.CascadeUUIDPrimaryKeyMixin

Utils for single and joined inheritance
---------------------------------------
* declarative.get_inherited_column
* declarative.get_inherited_primary_key
