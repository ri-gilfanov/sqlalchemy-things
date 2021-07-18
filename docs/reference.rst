Reference
=========
Custom column types
-------------------
.. autoclass:: sqlalchemy_things.column_types.UUIDType
  :show-inheritance:

Mixins for signle and joined inheritance
----------------------------------------
.. autoclass:: sqlalchemy_things.declarative.PolymorphicMixin
  :members:
  :show-inheritance:


Primary key mixins for signle and joined table inheritance
----------------------------------------------------------
.. autoclass:: sqlalchemy_things.declarative.BigIntegerPrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.DateTimePrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.IntegerPrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.UUIDPrimaryKeyMixin
  :members:
  :show-inheritance:


Primary key mixins for joined table inheritance
-----------------------------------------------
.. autoclass:: sqlalchemy_things.declarative.CascadeBigIntegerPrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.CascadeDateTimePrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.CascadeIntegerPrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.CascadeUUIDPrimaryKeyMixin
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.declarative.ParentPrimaryKeyMixin
  :members:
  :show-inheritance:


Pagination
----------
.. autoclass:: sqlalchemy_things.pagination.CountOffsetPage
  :members:
  :show-inheritance:

.. autoclass:: sqlalchemy_things.pagination.CountOffsetPaginator
  :members:
  :show-inheritance:


Utils for single and joined inheritance
---------------------------------------
.. autofunction:: sqlalchemy_things.declarative.get_inherited_column
.. autofunction:: sqlalchemy_things.declarative.get_inherited_primary_key
