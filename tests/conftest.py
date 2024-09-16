from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Awaitable, Callable

import pytest
import sqlalchemy as sa
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import Session

from sqlalchemy_things.declarative import IntegerPrimaryKeyMixin

if TYPE_CHECKING:  # pragma: no cover
    from sqlalchemy.engine.base import Engine


@pytest.fixture
def base_model() -> Any:
    class BaseModel(orm.DeclarativeBase): ...

    return BaseModel


@pytest.fixture
def sqlite_engine() -> AsyncEngine:
    return create_async_engine("sqlite+aiosqlite:///")


@pytest.fixture
def sqlite_sync_engine() -> Engine:
    return create_engine("sqlite:///")


@pytest.fixture
def sqlite_async_session_factory(
    sqlite_engine: AsyncEngine,
) -> orm.sessionmaker[AsyncSession]:  # type: ignore
    return orm.sessionmaker(sqlite_engine, class_=AsyncSession)  # type: ignore


@pytest.fixture
def sqlite_sync_session_factory(
    sqlite_sync_engine: Engine,
) -> orm.sessionmaker[Session]:
    return orm.sessionmaker(sqlite_sync_engine, class_=Session)


@pytest.fixture
def sqlite_async_session(sqlite_async_session_factory: Any) -> AsyncSession:
    return sqlite_async_session_factory()  # type: ignore


@pytest.fixture
def sqlite_sync_session(sqlite_sync_session_factory: Any) -> Session:
    return sqlite_sync_session_factory()  # type: ignore


@pytest.fixture
def mapped_class(base_model: type[Any]) -> type[IntegerPrimaryKeyMixin]:
    class MappedClass(base_model, IntegerPrimaryKeyMixin):  # type: ignore
        __tablename__ = "table_of_mapped_class"
        created_at = sa.Column(sa.DateTime, default=datetime.now)

    return MappedClass


@pytest.fixture
def init_db() -> Callable[..., Awaitable[None]]:
    async def create_tables(
        sqlite_engine: AsyncEngine,
        base_model: type[Any],
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
