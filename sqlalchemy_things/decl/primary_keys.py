import sqlalchemy as sa
from sqlalchemy import orm
from uuid import uuid4

from sqlalchemy_things.decl.abstract import DeclarativeMixin
from sqlalchemy_things.types import UUID


@orm.declarative_mixin
class Int32PKMixin(DeclarativeMixin):
    @orm.declared_attr
    def pk(cls):
        default = sa.Column(sa.Integer, primary_key=True)
        if hasattr(cls, '__table__'):
            return cls.__table__.c.get('pk', default)
        return default


@orm.declarative_mixin
class UUIDPKMixin(DeclarativeMixin):
    @orm.declared_attr
    def pk(cls):
        default = sa.Column(UUID, primary_key=True, default=uuid4)
        if hasattr(cls, '__table__'):
            return cls.__table__.c.get('pk', default)
        return default


@orm.declarative_mixin
class CascadeInt32PKMixin:
    @orm.declared_attr.cascading
    def pk(cls):
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.Integer, primary_key=True)

        for base in cls.__bases__:
            if hasattr(base, '__tablename__') and hasattr(base, 'pk'):
                table_name = getattr(base, '__tablename__')
                foreign_key = sa.ForeignKey(f'{table_name}.pk')
                return sa.Column(foreign_key, primary_key=True)


@orm.declarative_mixin
class CascadeUUIDPKMixin:
    @orm.declared_attr.cascading
    def pk(cls):
        if orm.has_inherited_table(cls) is False:
            return sa.Column(UUID, primary_key=True, default=uuid4)

        for base in cls.__bases__:
            if hasattr(base, '__tablename__') and hasattr(base, 'pk'):
                table_name = getattr(base, '__tablename__')
                foreign_key = sa.ForeignKey(f'{table_name}.pk')
                return sa.Column(foreign_key, primary_key=True)
