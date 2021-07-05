Reference
=========
Custom column types
-------------------
.. autoclass:: sqlalchemy_things.column_types.UUIDType

Mixins for signle and joined inheritance
----------------------------------------
.. autoclass:: sqlalchemy_things.declarative.PolymorphicMixin
  :members:


Primary key mixins for signle and joined table inheritance
----------------------------------------------------------
.. autoclass:: sqlalchemy_things.declarative.BigIntegerPrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.DateTimePrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.IntegerPrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.UUIDPrimaryKeyMixin
  :members:


Primary key mixins for joined table inheritance
-----------------------------------------------
.. autoclass:: sqlalchemy_things.declarative.CascadeBigIntegerPrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.CascadeDateTimePrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.CascadeIntegerPrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.CascadeUUIDPrimaryKeyMixin
  :members:

.. autoclass:: sqlalchemy_things.declarative.ParentPrimaryKeyMixin
  :members:


Utils for single and joined inheritance
---------------------------------------
.. autofunction:: sqlalchemy_things.declarative.get_inherited_column
.. autofunction:: sqlalchemy_things.declarative.get_inherited_primary_key
