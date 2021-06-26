from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects import postgresql
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.engine.interfaces import Dialect
    from typing import Optional


class UUID(TypeDecorator):
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect: 'Dialect'):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(postgresql.UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect: 'Dialect') -> 'Optional[str]':
        if value is None:
            return value
        if dialect.name == 'postgresql':
            return str(value)
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return f'{value.int:0>32x}'

    def process_result_value(self, value, dialect: 'Dialect') -> 'Optional[uuid.UUID]':
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
