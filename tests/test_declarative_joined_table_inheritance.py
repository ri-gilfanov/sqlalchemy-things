from typing import Any

import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine

from sqlalchemy_things.declarative import (
    CascadeBigIntegerPrimaryKeyMixin,
    CascadeIntegerPrimaryKeyMixin,
    CascadeUUIDPrimaryKeyMixin,
    PolymorphicMixin,
)


def get_child_models(base_model, primary_key_mixin):
    class Parent(base_model, primary_key_mixin, PolymorphicMixin):
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
    init_db,
):
    get_child_models(base_model, CascadeBigIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db,
):
    get_child_models(base_model, CascadeIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_test_with_uuid_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db,
):
    get_child_models(base_model, CascadeUUIDPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)
