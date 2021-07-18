Releases
========
Version 0.5.0
-------------
**Changed**

* Rename ``get_async`` attribute to ``get_page_async``
  in ``CountOffsetPaginator``;
* Rename ``get_sync`` attribute to ``get_page_sync``
  in ``CountOffsetPaginator``;

Version 0.4.0
-------------
**Added**

* ``CountOffsetPage``;
* ``CountOffsetPaginator``.

Version 0.3.0
-------------
**Changed**

* Rename ``definition`` attribute to ``discriminator`` in ``PolymorphicMixin``.

Version 0.2.0
-------------
**Changed**

* Rename `key` arg to `name` in ``declarative.get_inherited_column()``.

Version 0.1.0
-------------
**Changed**

* Rename ``CascadeDeclarativeMixin`` to ``InheritedDeclarativeMixin``;
* Rename ``InheritedPrimaryKeyMixin`` to ``ParentPrimaryKeyMixin``;
* Move ``ParentPrimaryKeyMixin`` from ``declarative.base`` to
  ``declarative.primary_keys``;
* Move ``get_inherited_primary_key`` from ``declarative.base`` to
  ``declarative.primary_keys``.
