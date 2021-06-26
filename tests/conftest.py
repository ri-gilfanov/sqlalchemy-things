import pytest
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


@pytest.fixture
def base_model():
    metadata = sa.MetaData()
    return orm.declarative_base(metadata=metadata)


@pytest.fixture
def sqlite_engine():
    return create_async_engine('sqlite+aiosqlite:///')


@pytest.fixture
def sqlite_session_factory(sqlite_engine):
    return orm.sessionmaker(sqlite_engine, AsyncSession)


@pytest.fixture
def sqlite_session(sqlite_session_factory):
    return sqlite_session_factory()
