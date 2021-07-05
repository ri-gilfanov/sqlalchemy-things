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

Documentation
-------------
https://sqlalchemy-things.readthedocs.io

Installation
------------
Installing ``sqlalchemy-things`` with pip: ::

  pip install sqlalchemy-things

Examples
--------
Single table inheritance
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

  from sqlalchemy_things.declarative import (
      IntegerPrimaryKeyMixin,
      PolymorphicMixin,
  )

  metadata = sa.MetaData()
  Base = orm.declarative_base(metadata=metadata)


  class Parent(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = 'single_table'


  class ChildA(Parent):
      __mapper_args__ = {'polymorphic_identity': 'child_a'}
      some_field = sa.Column(sa.String(255))


  class ChildB(Parent):
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      other_filed = sa.Column(sa.String(127))

Joined table inheritance with cascade primary key mixins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

  from sqlalchemy_things.declarative import (
      CascadeIntegerPrimaryKeyMixin,
      PolymorphicMixin,
  )

  metadata = sa.MetaData()
  Base = orm.declarative_base(metadata=metadata)


  class Parent(Base, CascadeIntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = 'cascade_pk_parent_table'


  class ChildA(Parent):
      __tablename__ = 'cascade_pk_child_table_a'
      __mapper_args__ = {'polymorphic_identity': 'child_a'}
      some_field = sa.Column(sa.String(255))


  class ChildB(Parent):
      __tablename__ = 'cascade_pk_child_table_b'
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      some_field = sa.Column(sa.String(127))


Joined table inheritance with simple primary key mixins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

  from sqlalchemy_things.declarative import (
      IntegerPrimaryKeyMixin,
      ParentPrimaryKeyMixin,
      PolymorphicMixin,
  )

  metadata = sa.MetaData()
  Base = orm.declarative_base(metadata=metadata)


  class Parent(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = 'inherited_pk_parent_table'


  class ChildA(ParentPrimaryKeyMixin, Parent):
      __tablename__ = 'inherited_pk_child_table_a'
      __mapper_args__ = {'polymorphic_identity': 'child_a'}
      some_field = sa.Column(sa.String(255))


  class ChildB(ParentPrimaryKeyMixin, Parent):
      __tablename__ = 'inherited_pk_child_table_b'
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      some_field = sa.Column(sa.String(127))
