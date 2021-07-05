Releases
========
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
