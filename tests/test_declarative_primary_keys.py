import uuid
from datetime import datetime
from typing import Any

import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy_things.declarative import (
    BigIntegerPrimaryKeyMixin,
    DateTimePrimaryKeyMixin,
    IntegerPrimaryKeyMixin,
    UUIDPrimaryKeyMixin,
)


@pytest.mark.asyncio
async def test_big_integer_primary_key(
    base_model: Any,
    sqlite_async_session: AsyncSession,
) -> None:
    class MyModel(base_model, BigIntegerPrimaryKeyMixin):  # type: ignore
        __tablename__ = "int64_pk_table"

    async with sqlite_async_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)  # type: ignore

    async with sqlite_async_session.begin():
        sqlite_async_session.add_all(
            [
                # SQLite unsupport BigInteger with autoincrement
                MyModel(pk=2**63 - 1),
            ]
        )

    async with sqlite_async_session.begin():
        result = await sqlite_async_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], int)


@pytest.mark.asyncio
async def test_datetime_primary_key(
    base_model: Any,
    sqlite_async_session: AsyncSession,
) -> None:
    class MyModel(base_model, DateTimePrimaryKeyMixin):  # type: ignore
        __tablename__ = "int64_pk_table"

    async with sqlite_async_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)  # type: ignore

    async with sqlite_async_session.begin():
        sqlite_async_session.add_all(
            [
                MyModel(),
            ]
        )

    async with sqlite_async_session.begin():
        result = await sqlite_async_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], datetime)


@pytest.mark.asyncio
async def test_integer_primary_key(
    base_model: Any,
    sqlite_async_session: AsyncSession,
) -> None:
    class MyModel(base_model, IntegerPrimaryKeyMixin):  # type: ignore
        __tablename__ = "int32_pk_table"

    async with sqlite_async_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)  # type: ignore

    async with sqlite_async_session.begin():
        sqlite_async_session.add_all(
            [
                MyModel(),
            ]
        )

    async with sqlite_async_session.begin():
        result = await sqlite_async_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], int)


@pytest.mark.asyncio
async def test_uuid_primary_key(
    base_model: Any,
    sqlite_async_session: AsyncSession,
) -> None:
    class MyModel(base_model, UUIDPrimaryKeyMixin):  # type: ignore
        __tablename__ = "my_table"

    async with sqlite_async_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)  # type: ignore

    async with sqlite_async_session.begin():
        sqlite_async_session.add_all(
            [
                MyModel(),
            ]
        )

    async with sqlite_async_session.begin():
        result = await sqlite_async_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], uuid.UUID)
