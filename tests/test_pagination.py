from datetime import datetime
from typing import Any

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import select

from sqlalchemy_things.pagination import OffsetPage, OffsetPaginator


@pytest.mark.asyncio
async def test_count_offset_page_async(
    base_model: Any,
    sqlite_async_session: AsyncSession,
    mapped_class: Any,
    init_db: Any,
) -> None:
    MAX_PAGE = 3
    session = sqlite_async_session

    await init_db(session.bind, base_model)
    async with session.begin():
        session.add_all([mapped_class() for i in range(42)])
        stmt = select(mapped_class)
        paginator = OffsetPaginator(max_page=MAX_PAGE)

        for number in range(5):
            page = await paginator.get_page_async(session, stmt, number)
            if number < 1 or number > MAX_PAGE:
                assert page is None
            else:
                assert isinstance(page, OffsetPage)
                items = tuple(page.items)
                for item in items:
                    assert isinstance(item, mapped_class)
                    assert isinstance(item.pk, int)
                    assert isinstance(item.created_at, datetime)

                if number <= 1:
                    assert page.previous is None
                elif number > 1 and len(page.items) > 0:
                    assert page.previous == number - 1
                else:
                    assert page.previous is None

                if number < page.last:
                    assert page.next == number + 1
                else:
                    assert page.next is None

                if number < page.last:
                    assert len(items) == page.page_size
                else:
                    assert len(items) == page.total % page.page_size


def test_count_offset_page_sync(
    base_model: Any,
    sqlite_sync_session: Session,
    mapped_class: Any,
    init_db_sync: Any,
) -> None:
    MAX_PAGE = 3
    session = sqlite_sync_session

    init_db_sync(session.bind, base_model)
    with session.begin():
        session.add_all([mapped_class() for i in range(42)])
        stmt = select(mapped_class)
        paginator = OffsetPaginator(max_page=MAX_PAGE)

        for number in range(5):
            page = paginator.get_page_sync(session, stmt, number)
            if number < 1 or number > MAX_PAGE:
                assert page is None
            else:
                assert isinstance(page, OffsetPage)
                items = tuple(page.items)
                for item in items:
                    assert isinstance(item, mapped_class)
                    assert isinstance(item.pk, int)
                    assert isinstance(item.created_at, datetime)

                if number <= 1:
                    assert page.previous is None
                elif number > 1 and len(page.items) > 0:
                    assert page.previous == number - 1
                else:
                    assert page.previous is None

                if number < page.last:
                    assert page.next == number + 1
                else:
                    assert page.next is None

                if number < page.last:
                    assert len(items) == page.page_size
                else:
                    assert len(items) == page.total % page.page_size
