from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest
import sqlalchemy as sa

from sqlalchemy_things.declarative import (
    BigIntegerPrimaryKeyMixin,
    DateTimePrimaryKeyMixin,
    DeclarativeMixin,
    IntegerPrimaryKeyMixin,
    PolymorphicMixin,
    UUIDPrimaryKeyMixin,
)

if TYPE_CHECKING:  # pragma: no cover
    from sqlalchemy.ext.asyncio import AsyncEngine


def get_child_models(
    base_model: Any,
    pk_mixin: type[DeclarativeMixin],
) -> tuple[Any, Any]:
    class Parent(base_model, pk_mixin, PolymorphicMixin):  # type: ignore
        __tablename__ = "single_table"

    class ChildA(Parent):
        __mapper_args__ = {"polymorphic_identity": "child_a"}
        some_field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __mapper_args__ = {"polymorphic_identity": "child_b"}
        other_field = sa.Column(sa.String(127))

    return ChildA, ChildB


@pytest.mark.asyncio
async def test_with_big_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, BigIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_datetime_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, DateTimePrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, IntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_uuid_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, UUIDPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)
