from typing import Any, Iterable

from sqlalchemy import Table, orm


@orm.declarative_mixin
class DeclarativeMixin:
    __table__: 'Table'


@orm.declarative_mixin
class CascadeDeclarativeMixin(DeclarativeMixin):
    __bases__: Iterable[Any]
