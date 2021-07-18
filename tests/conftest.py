from datetime import datetime
from typing import Any, Awaitable, Callable

import pytest
import sqlalchemy as sa
from sqlalchemy import create_engine, orm
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import Session

from sqlalchemy_things.declarative import IntegerPrimaryKeyMixin


@pytest.fixture
def metadata() -> sa.MetaData:
    return sa.MetaData()


@pytest.fixture
def base_model(metadata: sa.MetaData) -> orm.Mapper:
    return orm.declarative_base(metadata=metadata)


@pytest.fixture
def sqlite_engine() -> AsyncEngine:
    return create_async_engine('sqlite+aiosqlite:///')


@pytest.fixture
def sqlite_sync_engine() -> Engine:
    return create_engine('sqlite:///')


@pytest.fixture
def sqlite_async_session_factory(sqlite_engine: AsyncEngine) -> Any:
    return orm.sessionmaker(sqlite_engine, AsyncSession)


@pytest.fixture
def sqlite_sync_session_factory(sqlite_sync_engine: Engine) -> Any:
    return orm.sessionmaker(sqlite_sync_engine, Session)


@pytest.fixture
def sqlite_async_session(sqlite_async_session_factory: Any) -> AsyncSession:
    return sqlite_async_session_factory()


@pytest.fixture
def sqlite_sync_session(sqlite_sync_session_factory: Any) -> Session:
    return sqlite_sync_session_factory()


@pytest.fixture
def mapped_class(base_model: orm.Mapper) -> AsyncSession:
    class MappedClass(base_model, IntegerPrimaryKeyMixin):  # type: ignore
        __tablename__ = 'table_of_mapped_class'
        created_at = sa.Column(sa.DateTime, default=datetime.now)
    return MappedClass


@pytest.fixture
def init_db() -> Callable[..., Awaitable[None]]:
    async def create_tables(
        sqlite_engine: AsyncEngine,
        base_model: Any,
    ) -> None:
        async with sqlite_engine.begin() as conn:
            await conn.run_sync(base_model.metadata.create_all)
    return create_tables


@pytest.fixture
def init_db_sync() -> Callable[[Engine, Any], None]:
    def create_tables(
        sqlite_sync_engine: Engine,
        base_model: Any,
    ) -> None:
        base_model.metadata.create_all(sqlite_sync_engine)
    return create_tables
