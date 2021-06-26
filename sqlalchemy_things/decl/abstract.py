from sqlalchemy import Table, orm


@orm.declarative_mixin
class DeclarativeMixin:
    __table__: 'Table'
