from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

import sqlalchemy as sa
from sqlalchemy import orm

if TYPE_CHECKING:
    from collections.abc import Iterable

    from sqlalchemy.sql.selectable import FromClause


@orm.declarative_mixin
class DeclarativeMixin:
    __table__: ClassVar[FromClause]


@orm.declarative_mixin
class InheritedDeclarativeMixin(DeclarativeMixin):
    __bases__: Iterable[Any]


@orm.declarative_mixin
class PolymorphicMixin(DeclarativeMixin):
    """Polymorphic mixin for single table and joined table inheritance."""

    @orm.declared_attr
    def discriminator(self) -> orm.Mapped[str]:
        return orm.mapped_column("discriminator", sa.String(40), nullable=False)

    __mapper_args__ = {
        "polymorphic_on": "discriminator",
    }


def get_inherited_column(
    self: DeclarativeMixin,
    name: str,
    default: orm.Mapped[Any],
) -> orm.Mapped[Any]:
    """
    Utility function for column inheriting in mixins.

    :param name: column name of parent class;
    :param default: default value if not found in parent class.
    """
    if hasattr(self, "__table__"):
        return self.__table__.c.get(name, default)  # type: ignore
    return default
