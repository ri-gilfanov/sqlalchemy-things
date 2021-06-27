from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_things.declarative.abstract import (
    CascadeDeclarativeMixin,
    DeclarativeMixin,
)
from sqlalchemy_things.declarative.inheritance import get_inherited_primary_key
from sqlalchemy_things.types import UUIDType


@orm.declarative_mixin
class BigIntegerPrimaryKeyMixin(DeclarativeMixin):
    @orm.declared_attr
    def pk(cls) -> sa.Column:
        default = sa.Column(sa.BigInteger, primary_key=True)
        if hasattr(cls, '__table__'):
            return cls.__table__.c.get('pk', default)
        return default


@orm.declarative_mixin
class CascadeBigIntegerPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.BigInteger, primary_key=True)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class IntegerPrimaryKeyMixin(DeclarativeMixin):
    @orm.declared_attr
    def pk(cls) -> sa.Column:
        default = sa.Column(sa.Integer, primary_key=True)
        if hasattr(cls, '__table__'):
            return cls.__table__.c.get('pk', default)
        return default


@orm.declarative_mixin
class CascadeIntegerPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(sa.Integer, primary_key=True)
        return get_inherited_primary_key(cls)


@orm.declarative_mixin
class UUIDPrimaryKeyMixin(DeclarativeMixin):
    @orm.declared_attr
    def pk(cls) -> sa.Column:
        default = sa.Column(UUIDType, primary_key=True, default=uuid4)
        if hasattr(cls, '__table__'):
            return cls.__table__.c.get('pk', default)
        return default


@orm.declarative_mixin
class CascadeUUIDPrimaryKeyMixin(CascadeDeclarativeMixin):
    @orm.declared_attr.cascading
    def pk(cls) -> sa.Column:
        if orm.has_inherited_table(cls) is False:
            return sa.Column(UUIDType, primary_key=True, default=uuid4)
        return get_inherited_primary_key(cls)
