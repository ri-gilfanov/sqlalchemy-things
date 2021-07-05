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
    definition = sa.Column(sa.String(40), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': definition,
    }


def get_inherited_column(
    cls: Any,
    key: str,
    default: sa.Column,
) -> Optional[sa.Column]:
    """Utility function for column inheriting in mixins."""
    if hasattr(cls, '__table__'):
        return cls.__table__.c.get(key, default)
    return None
