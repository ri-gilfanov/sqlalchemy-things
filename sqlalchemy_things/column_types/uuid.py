import uuid
from typing import Any, Optional, Union

from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.types import CHAR, TypeDecorator


class UUIDType(TypeDecorator):  # type: ignore
    """Backend-agnostic UUID type."""
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect: Dialect) -> Any:
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(postgresql.UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(
        self,
        value: Union[int, str, uuid.UUID],
        dialect: Dialect,
    ) -> Optional[str]:
        if value is None:
            return value
        if dialect.name == 'postgresql':
            return str(value)
        if isinstance(value, str):
            value = uuid.UUID(value)
        if isinstance(value, uuid.UUID):
            return f'{value.int:0>32x}'
        raise TypeError

    def process_result_value(
        self,
        value: Optional[Union[str, uuid.UUID]],
        dialect: 'Dialect',
    ) -> 'Optional[uuid.UUID]':
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
