from typing import Any, Iterable, Optional

import sqlalchemy as sa
from sqlalchemy import Table, orm


@orm.declarative_mixin
class DeclarativeMixin:
    __table__: 'Table'


@orm.declarative_mixin
class CascadeDeclarativeMixin(DeclarativeMixin):
    __bases__: Iterable[Any]


@orm.declarative_mixin
class PolymorphicMixin(DeclarativeMixin):
    definition = sa.Column(sa.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': definition,
    }


def get_inherited_column(
    cls: Any,
    key: str,
    default: sa.Column,
) -> Optional[sa.Column]:
    if hasattr(cls, '__table__'):
        return cls.__table__.c.get(key, default)
    return None


def get_inherited_primary_key(cls: Any) -> Optional[sa.Column]:
    for base in cls.__bases__:
        # TODO: after dropped Python 3.7
        # if table_name := getattr(base, '__tablename__'):
        if getattr(base, '__tablename__'):
            table_name = getattr(base, '__tablename__')
            foreign_key = sa.ForeignKey(f'{table_name}.pk')
            return sa.Column(foreign_key, primary_key=True)
    return None


@orm.declarative_mixin
class InheritedPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading  # type: ignore
    def pk(cls) -> sa.Column:
        return get_inherited_primary_key(cls)
