=================
sqlalchemy-things
=================
|ReadTheDocs| |PyPI release| |License| |Python versions| |PyPI downloads| |GitHub CI|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/sqlalchemy-things/badge/?version=latest
  :target: https://sqlalchemy-things.readthedocs.io/en/latest/?badge=latest
  :alt: Read The Docs build

.. |PyPI release| image:: https://badge.fury.io/py/sqlalchemy-things.svg
  :target: https://pypi.org/project/sqlalchemy-things/
  :alt: Release

.. |License| image:: https://img.shields.io/badge/License-MIT-green
  :target: https://github.com/ri-gilfanov/sqlalchemy-things/blob/master/LICENSE
  :alt: MIT License

.. |Python versions| image:: https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue
  :target: https://pypi.org/project/sqlalchemy-things/
  :alt: Python version support

.. |PyPI downloads| image:: https://static.pepy.tech/personalized-badge/sqlalchemy-things?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads
  :target: https://pepy.tech/project/sqlalchemy-things
  :alt: PyPI downloads count

.. |GitHub CI| image:: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml/badge.svg?branch=master
  :target: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml
  :alt: GitHub continuous integration

Utility collection for development with `SQLAlchemy 2.0
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

  from sqlalchemy import orm
  from sqlalchemy_things.declarative import (
      IntegerPrimaryKeyMixin,
      PolymorphicMixin,
  )

  class Base(orm.DeclarativeBase): ...


  class ParentA(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = "single_table"


  class ChildA1(ParentA):
      __mapper_args__ = {"polymorphic_identity": "child_a1"}
      some_field = sa.Column(sa.String(255))


  class ChildA2(ParentA):
      __mapper_args__ = {"polymorphic_identity": "child_a2"}
      other_filed = sa.Column(sa.String(127))

Joined table inheritance with cascade primary key mixins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

  from sqlalchemy import orm
  from sqlalchemy_things.declarative import (
      CascadeIntegerPrimaryKeyMixin,
      PolymorphicMixin,
  )

  class Base(orm.DeclarativeBase): ...


  class ParentB(Base, CascadeIntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = "parent_b"


  class ChildB1(ParentB):
      __tablename__ = "child_b1"
      __mapper_args__ = {"polymorphic_identity": "child_b1"}
      some_field = sa.Column(sa.String(255))


  class ChildB2(ParentB):
      __tablename__ = "child_b2"
      __mapper_args__ = {"polymorphic_identity": "child_b2"}
      some_field = sa.Column(sa.String(127))


Joined table inheritance with simple primary key mixins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

  from sqlalchemy import orm
  from sqlalchemy_things.declarative import (
      IntegerPrimaryKeyMixin,
      ParentPrimaryKeyMixin,
      PolymorphicMixin,
  )

  class Base(orm.DeclarativeBase): ...


  class ParentC(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
      __tablename__ = "parent_c"


  class ChildC1(ParentPrimaryKeyMixin, ParentC):
      __tablename__ = "child_c1"
      __mapper_args__ = {"polymorphic_identity": "child_c1"}
      some_field = sa.Column(sa.String(255))


  class ChildC2(ParentPrimaryKeyMixin, ParentC):
      __tablename__ = "child_c2"
      __mapper_args__ = {"polymorphic_identity": "child_c2"}
      some_field = sa.Column(sa.String(127))
