import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_things.declarative import (
    CascadeDeclarativeMixin,
    DeclarativeMixin,
)


@orm.declarative_mixin
class PolymorphicMixin(DeclarativeMixin):
    definition = sa.Column(sa.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': definition,
    }


def get_inherited_column(cls, key, default):
    if hasattr(cls, '__table__'):
        return cls.__table__.c.get(key, default)


def get_inherited_primary_key(cls):
    for base in cls.__bases__:
        if hasattr(base, '__tablename__') and hasattr(base, 'pk'):
            table_name = getattr(base, '__tablename__')
            foreign_key = sa.ForeignKey(f'{table_name}.pk')
            return sa.Column(foreign_key, primary_key=True)


@orm.declarative_mixin
class InheritedPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading
    def pk(cls) -> sa.Column:
        return get_inherited_primary_key(cls)
