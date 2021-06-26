import uuid

import pytest
import sqlalchemy as sa

from sqlalchemy_things.declarative import (
    BigIntegerPrimaryKeyMixin,
    IntegerPrimaryKeyMixin,
    UUIDPrimaryKeyMixin,
)


@pytest.mark.asyncio
async def test_big_integer_primary_key(base_model, sqlite_session):
    class MyModel(base_model, BigIntegerPrimaryKeyMixin):
        __tablename__ = 'int32_pk_table'

    async with sqlite_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            MyModel(pk=1),  # SQLite not support autoincrement for big integer
        ])

    async with sqlite_session.begin():
        result = await sqlite_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], int)


@pytest.mark.asyncio
async def test_integer_primary_key(base_model, sqlite_session):
    class MyModel(base_model, IntegerPrimaryKeyMixin):
        __tablename__ = 'int32_pk_table'

    async with sqlite_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            MyModel(),
        ])

    async with sqlite_session.begin():
        result = await sqlite_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], int)


@pytest.mark.asyncio
async def test_uuid_primary_key(base_model, sqlite_session):
    class MyModel(base_model, UUIDPrimaryKeyMixin):
        __tablename__ = 'my_table'

    async with sqlite_session.bind.begin() as connection:
        await connection.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            MyModel(),
        ])

    async with sqlite_session.begin():
        result = await sqlite_session.execute(sa.select(MyModel))
        data = [record.pk for record in result.scalars()]
        assert isinstance(data[0], uuid.UUID)
