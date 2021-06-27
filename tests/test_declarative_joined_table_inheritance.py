from typing import Any, Tuple, Type

import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine

from sqlalchemy_things.declarative import (
    CascadeBigIntegerPrimaryKeyMixin,
    CascadeDateTimePrimaryKeyMixin,
    CascadeDeclarativeMixin,
    CascadeIntegerPrimaryKeyMixin,
    CascadeUUIDPrimaryKeyMixin,
    PolymorphicMixin,
)


def get_child_models(
    base_model: Any,
    pk_mixin: Type[CascadeDeclarativeMixin],
) -> Tuple[Any, Any]:
    class Parent(base_model, pk_mixin, PolymorphicMixin):  # type: ignore
        __tablename__ = 'parent_table'

    class ChildA(Parent):
        __tablename__ = 'child_table_a'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __tablename__ = 'child_table_b'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field = sa.Column(sa.String(127))

    return ChildA, ChildB


@pytest.mark.asyncio
async def test_with_big_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, CascadeBigIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_datetime_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, CascadeDateTimePrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, CascadeIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_test_with_uuid_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_child_models(base_model, CascadeUUIDPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)
