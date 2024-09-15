from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

from sqlalchemy.dialects import postgresql
from sqlalchemy.types import CHAR, TypeDecorator

if TYPE_CHECKING:  # pragma: no cover
    from sqlalchemy.engine.interfaces import Dialect


class UUIDType(TypeDecorator[UUID]):
    """Backend-agnostic UUID type."""

    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect: Dialect) -> Any:
        if dialect.name == "postgresql":
            return dialect.type_descriptor(postgresql.UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(
        self,
        value: int | str | UUID,  # type: ignore
        dialect: Dialect,
    ) -> str | None:
        if value is None:
            return value
        if dialect.name == "postgresql":
            return str(value)
        if isinstance(value, str):
            value = UUID(value)
        if isinstance(value, UUID):
            return f"{value.int:0>32x}"
        raise TypeError

    def process_result_value(
        self,
        value: str | UUID | None,
        dialect: Dialect,
    ) -> UUID | None:
        if value is None:
            return value
        if not isinstance(value, UUID):
            value = UUID(value)
        return value
