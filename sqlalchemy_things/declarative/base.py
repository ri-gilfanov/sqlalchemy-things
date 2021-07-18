from typing import Any, Iterable, Optional

import sqlalchemy as sa
from sqlalchemy import Table, orm


@orm.declarative_mixin
class DeclarativeMixin:
    __table__: 'Table'


@orm.declarative_mixin
class InheritedDeclarativeMixin(DeclarativeMixin):
    __bases__: Iterable[Any]


@orm.declarative_mixin
class PolymorphicMixin(DeclarativeMixin):
    """Polymorphic mixin for single table and joined table inheritance."""
    discriminator = sa.Column(sa.String(40), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': discriminator,
    }


def get_inherited_column(
    cls: Any,
    name: str,
    default: sa.Column,
) -> Optional[sa.Column]:
    """
    Utility function for column inheriting in mixins.

    :param name: column name of parent class;
    :param default: default value if not found in parent class.
    """
    if hasattr(cls, '__table__'):
        return cls.__table__.c.get(name, default)
    return None
