from typing import Any, Tuple, Type

import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine

from sqlalchemy_things.declarative import (
    BigIntegerPrimaryKeyMixin,
    CascadeBigIntegerPrimaryKeyMixin,
    CascadeDateTimePrimaryKeyMixin,
    CascadeIntegerPrimaryKeyMixin,
    CascadeUUIDPrimaryKeyMixin,
    DateTimePrimaryKeyMixin,
    DeclarativeMixin,
    InheritedDeclarativeMixin,
    IntegerPrimaryKeyMixin,
    ParentPrimaryKeyMixin,
    PolymorphicMixin,
    UUIDPrimaryKeyMixin,
)


def get_cascade_pk_child_models(
    base_model: Any,
    pk_mixin: Type[InheritedDeclarativeMixin],
) -> Tuple[Any, Any]:
    class Parent(base_model, pk_mixin, PolymorphicMixin):  # type: ignore
        __tablename__ = 'cascade_pk_parent_table'

    class ChildA(Parent):
        __tablename__ = 'cascade_pk_child_table_a'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        some_field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __tablename__ = 'cascade_pk_child_table_b'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        some_field = sa.Column(sa.String(127))

    return ChildA, ChildB


def get_inherited_pk_child_models(
    base_model: Any,
    pk_mixin: Type[DeclarativeMixin],
) -> Tuple[Any, Any]:
    class Parent(base_model, pk_mixin, PolymorphicMixin):  # type: ignore
        __tablename__ = 'inherited_pk_parent_table'

    class ChildA(ParentPrimaryKeyMixin, Parent):
        __tablename__ = 'inherited_pk_child_table_a'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        some_field = sa.Column(sa.String(255))

    class ChildB(ParentPrimaryKeyMixin, Parent):
        __tablename__ = 'inherited_pk_child_table_b'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        some_field = sa.Column(sa.String(127))
    return ChildA, ChildB


@pytest.mark.asyncio
async def test_with_cascade_big_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_cascade_pk_child_models(base_model, CascadeBigIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_inherited_big_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_inherited_pk_child_models(base_model, BigIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_cascade_datetime_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_cascade_pk_child_models(base_model, CascadeDateTimePrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_inherited_datetime_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_inherited_pk_child_models(base_model, DateTimePrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_cascade_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_cascade_pk_child_models(base_model, CascadeIntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_inherited_integer_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_inherited_pk_child_models(base_model, IntegerPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_cascade_uuid_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_cascade_pk_child_models(base_model, CascadeUUIDPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)


@pytest.mark.asyncio
async def test_with_inherited_uuid_pk(
    base_model: Any,
    sqlite_engine: AsyncEngine,
    init_db: Any,
) -> None:
    get_inherited_pk_child_models(base_model, UUIDPrimaryKeyMixin)
    await init_db(sqlite_engine, base_model)
