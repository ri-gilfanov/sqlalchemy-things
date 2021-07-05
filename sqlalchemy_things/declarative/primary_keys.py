from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_things.column_types import UUIDType
from sqlalchemy_things.declarative.base import (
    DeclarativeMixin,
    InheritedDeclarativeMixin,
    get_inherited_column,
)


@orm.declarative_mixin
class BigIntegerPrimaryKeyMixin(DeclarativeMixin):
    """
    Big integer primary key mixin.

    .. warning::
      SQLite backend not support autoincrement for BigInteger column type.
    """
    @orm.declared_attr  # type: ignore
    def pk(cls) -> sa.Column:
        default = sa.Column(sa.BigInteger, primary_key=True)
        get_inherited_column(cls, 'pk', default)
        return default


@orm.declarative_mixin
class CascadeBigIntegerPrimaryKeyMixin(InheritedDeclarativeMixin):
    """
    Cascade big integer primary key mixin for joined table inheritance.

    .. warning::
      SQLite backend not support autoincrement for BigInteger column type.
    """
    @orm.declared_attr.cascading  # type: ignore
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.BigInteger, primary_key=True)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class CascadeDateTimePrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade datetime primary key mixin for joined table inheritance."""
    @orm.declared_attr.cascading  # type: ignore
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.DateTime, primary_key=True,
                             default=datetime.now)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class CascadeIntegerPrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade integer primary key mixin for joined table inheritance."""
    @orm.declared_attr.cascading  # type: ignore
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.Integer, primary_key=True)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class CascadeUUIDPrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade UUID primary key mixin for joined table inheritance."""
    @orm.declared_attr.cascading  # type: ignore
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(UUIDType, primary_key=True, default=uuid4)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class DateTimePrimaryKeyMixin(DeclarativeMixin):
    """Datetime primary key mixin."""
    @orm.declared_attr  # type: ignore
    def pk(cls) -> sa.Column:
        default = sa.Column(sa.DateTime, primary_key=True, default=datetime.now)
        get_inherited_column(cls, 'pk', default)
        return default


@orm.declarative_mixin
class IntegerPrimaryKeyMixin(DeclarativeMixin):
    """Integer primary key mixin."""
    @orm.declared_attr  # type: ignore
    def pk(cls) -> sa.Column:
        default = sa.Column(sa.Integer, primary_key=True)
        get_inherited_column(cls, 'pk', default)
        return default


@orm.declarative_mixin
class ParentPrimaryKeyMixin(InheritedDeclarativeMixin):
    """
    Parent primary key mixin for child class in joined table inheritance without
    cascade primary key mixin.

    .. warning::
      This mixin must precede the parent class when declaring a child class.
    """
    @orm.declared_attr  # type: ignore
    def pk(cls) -> sa.Column:
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class UUIDPrimaryKeyMixin(DeclarativeMixin):
    """UUID primary key mixin."""
    @orm.declared_attr  # type: ignore
    def pk(cls) -> sa.Column:
        default = sa.Column(UUIDType, primary_key=True, default=uuid4)
        get_inherited_column(cls, 'pk', default)
        return default


def get_inherited_primary_key(cls: Any) -> Optional[sa.Column]:
    """
    Utility function for creating child primary key in joined table inheritance.
    """
    for base in cls.__bases__:
        # TODO: after dropped Python 3.7
        # if table_name := getattr(base, '__tablename__'):
        if hasattr(base, '__tablename__'):
            table_name = getattr(base, '__tablename__')
            foreign_key = sa.ForeignKey(f'{table_name}.pk')
            return sa.Column(foreign_key, primary_key=True)
    return None
