from typing import Any, Awaitable, Callable

import pytest
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)


@pytest.fixture
def base_model() -> orm.Mapper:
    metadata = sa.MetaData()
    return orm.declarative_base(metadata=metadata)


@pytest.fixture
def sqlite_engine() -> AsyncEngine:
    return create_async_engine('sqlite+aiosqlite:///')


@pytest.fixture
def sqlite_session_factory(sqlite_engine: AsyncEngine) -> Any:
    return orm.sessionmaker(sqlite_engine, AsyncSession)


@pytest.fixture
def sqlite_session(sqlite_session_factory: Any) -> AsyncSession:
    return sqlite_session_factory()


@pytest.fixture
def init_db() -> Callable[..., Awaitable[None]]:
    async def create_tables(
        sqlite_engine: AsyncEngine,
        base_model: Any,
    ) -> None:
        async with sqlite_engine.begin() as conn:
            await conn.run_sync(base_model.metadata.create_all)
    return create_tables
