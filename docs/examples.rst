Examples
========
Single table inheritance
------------------------
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
      field_a = sa.Column(sa.String(255))


  class ChildB(Parent):
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      field_b = sa.Column(sa.String(127))


Joined table inheritance with cascade primary key mixins
--------------------------------------------------------
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
      field = sa.Column(sa.String(255))


  class ChildB(Parent):
      __tablename__ = 'cascade_pk_child_table_b'
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      field = sa.Column(sa.String(127))


Joined table inheritance with simple primary key mixins
-------------------------------------------------------
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
      field = sa.Column(sa.String(255))


  class ChildB(ParentPrimaryKeyMixin, Parent):
      __tablename__ = 'inherited_pk_child_table_b'
      __mapper_args__ = {'polymorphic_identity': 'child_b'}
      field = sa.Column(sa.String(127))
