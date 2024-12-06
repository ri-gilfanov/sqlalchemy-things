Releases
========
Version 1.1.0
-------------
**Changed**

* Update dependencies.

**Removed**

* Dropped support for Python 3.8.

Version 1.0.2
-------------

**Added**

* Added support for Python 3.13.

**Changed**

* Update dependencies.

Version 1.0.1
-------------

**Changed**

* Fix ``table`` type hint for ``base.DeclarativeMixin``.

Version 1.0.0
-------------

**Added**

* Added support for Python 3.11 and 3.12;
* Added support for SQLAlchemy v2.0.

**Changed**

* Renamed first argument from ``cls`` to ``self`` in signatures of
  ``get_inherited_column()`` and ``get_inherited_primary_key()`` functions.

**Removed**

* Dropped support for Python 3.7;
* Dropped support for SQLAlchemy 1.4.

Version 0.10.0
--------------
**Added**

* Handling ``number`` < 1 for ``pagination.OffsetPaginator.get_page_async()``
  and ``pagination.OffsetPaginator.get_page_sync``.

**Changed**

* renamed ``page_number`` to ``number`` for ``pagination`` classes;
* renamed ``total_items`` to ``total`` for ``pagination`` classes.

Version 0.9.0
-------------
**Changed**

* ``ValueError`` exception replaced with return ``None`` when exceeding
  the ``max_page`` in ``pagination.OffsetPage``.

Version 0.8.0
-------------
**Added**

* ``pagination.OffsetPage``.

**Changed**

* Renamed ``prepare_page_async()`` method to ``get_page_async()``
  in ``pagination.OffsetPaginator``;
* Renamed ``prepare_page_sync()`` method to ``get_page_sync()``
  in ``pagination.OffsetPaginator``.

  **Removed**
  
* ``get_items()`` method from ``pagination.OffsetPaginator``;
* ``get_last_page_number()`` method from ``pagination.OffsetPaginator``;
* ``get_next_page_number()`` method from ``pagination.OffsetPaginator``;
* ``get_previous_page_number()`` method from ``pagination.OffsetPaginator``.

Version 0.7.0
-------------
**Added**

* ``get_items()`` method for ``pagination.OffsetPaginator``;
* ``get_last_page_number()`` method for ``pagination.OffsetPaginator``;
* ``get_next_page_number()`` method for ``pagination.OffsetPaginator``;
* ``get_previous_page_number()`` method for ``pagination.OffsetPaginator``.

**Changed**

* Renamed ``get_page_async`` method to ``prepare_page_async``
  in ``pagination.OffsetPaginator``;
* Renamed ``get_page_sync`` method to ``prepare_page_sync``
  in ``pagination.OffsetPaginator``.

**Removed**

* ``pagination.OffsetPage``.

Version 0.6.0
-------------
**Added**

* ``max_page`` attribute for ``pagination.OffsetPaginator``.

**Changed**

* Renamed ``next`` attribute to ``next_number`` in ``pagination.OffsetPage``;
* Renamed ``previous`` attribute to ``previous_number``
  in ``pagination.OffsetPage``;
* Renamed ``limit`` attribute to ``page_size``
  in ``pagination.OffsetPaginator``.

Version 0.5.0
-------------
**Changed**

* Renamed ``pagination.CountOffsetPage`` to ``pagination.OffsetPage``;
* Renamed ``pagination.CountOffsetPaginator`` to ``pagination.OffsetPaginator``;
* Renamed ``get_async`` method to ``get_page_async``
  in ``pagination.OffsetPaginator``;
* Renamed ``get_sync`` method to ``get_page_sync``
  in ``pagination.OffsetPaginator``.

Version 0.4.0
-------------
**Added**

* ``pagination.CountOffsetPage``;
* ``pagination.CountOffsetPaginator``.

Version 0.3.0
-------------
**Changed**

* Rename ``definition`` attribute to ``discriminator``
  in ``declarative.PolymorphicMixin``.

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
