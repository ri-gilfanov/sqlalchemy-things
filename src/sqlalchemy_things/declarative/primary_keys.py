from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

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

    @orm.declared_attr
    def pk(self) -> orm.Mapped[int]:
        default = orm.mapped_column("pk", sa.BigInteger, primary_key=True)
        return get_inherited_column(self, "pk", default)


@orm.declarative_mixin
class CascadeBigIntegerPrimaryKeyMixin(InheritedDeclarativeMixin):
    """
    Cascade big integer primary key mixin for joined table inheritance.

    .. warning::
      SQLite backend not support autoincrement for BigInteger column type.
    """

    @orm.declared_attr.cascading  # type: ignore
    def pk(self) -> orm.Mapped[int]:
        if orm.has_inherited_table(self) is False:  # type: ignore
            return orm.mapped_column("pk", sa.BigInteger, primary_key=True)
        return get_inherited_primary_key(self)


@orm.declarative_mixin
class CascadeDateTimePrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade datetime primary key mixin for joined table inheritance."""

    @orm.declared_attr.cascading  # type: ignore
    def pk(self) -> orm.Mapped[datetime]:
        if orm.has_inherited_table(self) is False:  # type: ignore
            return orm.mapped_column(
                "pk", sa.DateTime, primary_key=True, default=datetime.now
            )
        return get_inherited_primary_key(self)


@orm.declarative_mixin
class CascadeIntegerPrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade integer primary key mixin for joined table inheritance."""

    @orm.declared_attr.cascading  # type: ignore
    def pk(self) -> orm.Mapped[int]:
        if orm.has_inherited_table(self) is False:  # type: ignore
            return orm.mapped_column("pk", sa.Integer, primary_key=True)
        return get_inherited_primary_key(self)


@orm.declarative_mixin
class CascadeUUIDPrimaryKeyMixin(InheritedDeclarativeMixin):
    """Cascade UUID primary key mixin for joined table inheritance."""

    @orm.declared_attr.cascading  # type: ignore
    def pk(self) -> orm.Mapped[UUID]:
        if orm.has_inherited_table(self) is False:  # type: ignore
            return orm.mapped_column("pk", UUIDType, primary_key=True, default=uuid4)
        return get_inherited_primary_key(self)


@orm.declarative_mixin
class DateTimePrimaryKeyMixin(DeclarativeMixin):
    """Datetime primary key mixin."""

    @orm.declared_attr
    def pk(self) -> orm.Mapped[datetime]:
        default = orm.mapped_column(
            "pk", sa.DateTime, primary_key=True, default=datetime.now
        )
        return get_inherited_column(self, "pk", default)


@orm.declarative_mixin
class IntegerPrimaryKeyMixin(DeclarativeMixin):
    """Integer primary key mixin."""

    @orm.declared_attr
    def pk(self) -> orm.Mapped[int]:
        default = orm.mapped_column("pk", sa.Integer, primary_key=True)
        return get_inherited_column(self, "pk", default)


@orm.declarative_mixin
class ParentPrimaryKeyMixin(InheritedDeclarativeMixin):
    """
    Parent primary key mixin for child class in joined table inheritance without
    cascade primary key mixin.

    .. warning::
      This mixin must precede the parent class when declaring a child class.
    """

    @orm.declared_attr
    def pk(self) -> orm.Mapped[Any]:
        return get_inherited_primary_key(self)


@orm.declarative_mixin
class UUIDPrimaryKeyMixin(DeclarativeMixin):
    """UUID primary key mixin."""

    @orm.declared_attr
    def pk(self) -> orm.Mapped[UUID]:
        default = orm.mapped_column("pk", UUIDType, primary_key=True, default=uuid4)
        return get_inherited_column(self, "pk", default)


def get_inherited_primary_key(self: Any) -> orm.Mapped[Any]:
    """
    Utility function for creating child primary key in joined table inheritance.
    """
    if orm.has_inherited_table(self) is False:
        raise ValueError
    column = None
    for base in self.__bases__:
        if table_name := getattr(base, "__tablename__", None):
            column = orm.mapped_column(
                "pk", sa.ForeignKey(f"{table_name}.pk"), primary_key=True
            )
    if not column:
        raise ValueError
    return column
