from datetime import datetime
from typing import Any

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import select

from sqlalchemy_things.pagination import OffsetPaginator


@pytest.mark.asyncio
async def test_count_offset_page_async(
    base_model: Any,
    sqlite_async_session: AsyncSession,
    mapped_class: Any,
    init_db: Any,
) -> None:
    await init_db(sqlite_async_session.bind, base_model)
    async with sqlite_async_session.begin():
        sqlite_async_session.add_all([
            mapped_class()
            for i in range(92)
        ])
        stmt = select(mapped_class)
        paginator = OffsetPaginator(max_page=10)

        page = await paginator.get_page_async(sqlite_async_session, stmt, 1)
        items = tuple(page.items)
        for item in items:
            assert isinstance(item, mapped_class)
            assert isinstance(item.pk, int)
            assert isinstance(item.created_at, datetime)
        assert page.previous is None
        assert page.next == 2
        assert page.last == 10
        assert len(items) == 10
        assert page.total_items == 92

        page = await paginator.get_page_async(sqlite_async_session, stmt, 5)
        assert page.previous == 4
        assert page.next == 6
        assert len(tuple(page.items)) == 10

        page = await paginator.get_page_async(sqlite_async_session, stmt, 10)
        assert page.previous == 9
        assert page.next is None
        assert len(tuple(page.items)) == 2

        page = await paginator.get_page_async(sqlite_async_session, stmt, 11)
        assert page is None


def test_count_offset_page_sync(
    base_model: Any,
    sqlite_sync_session: Session,
    mapped_class: Any,
    init_db_sync: Any,
) -> None:
    init_db_sync(sqlite_sync_session.bind, base_model)
    with sqlite_sync_session.begin():
        sqlite_sync_session.add_all([
            mapped_class()
            for i in range(92)
        ])
        stmt = select(mapped_class)
        paginator = OffsetPaginator(max_page=10)

        page = paginator.get_page_sync(sqlite_sync_session, stmt, 1)
        items = tuple(page.items)
        for item in items:
            assert isinstance(item, mapped_class)
            assert isinstance(item.pk, int)
            assert isinstance(item.created_at, datetime)
        assert page.previous is None
        assert page.next == 2
        assert page.last == 10
        assert len(items) == 10
        assert page.total_items == 92

        page = paginator.get_page_sync(sqlite_sync_session, stmt, 5)
        assert page.previous == 4
        assert page.next == 6
        assert len(tuple(page.items)) == 10

        page = paginator.get_page_sync(sqlite_sync_session, stmt, 10)
        assert page.previous == 9
        assert page.next is None
        assert len(tuple(page.items)) == 2

        page = paginator.get_page_sync(sqlite_sync_session, stmt, 11)
        assert page is None
