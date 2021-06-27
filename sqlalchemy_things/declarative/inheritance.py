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


@orm.declarative_mixin
class InheritedPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading
    def pk(cls) -> sa.Column:
        for base in cls.__bases__:
            if hasattr(base, '__tablename__') and hasattr(base, 'pk'):
                table_name = getattr(base, '__tablename__')
                foreign_key = sa.ForeignKey(f'{table_name}.pk')
                return sa.Column(foreign_key, primary_key=True)
