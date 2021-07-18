from typing import Optional, Union

from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncScalarResult, AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select, select
from sqlalchemy.sql.functions import count


class CountOffsetPage:
    def __init__(
        self,
        items: Union[AsyncScalarResult, ScalarResult],
        next: Optional[int],
        previous: Optional[int],
        total_items: int,
    ):
        self.items = items
        self.next = next
        self.previous = previous
        self.total_items = total_items


class CountOffsetPaginator:
    def __init__(self, limit: int = 10):
        self.limit = limit

    async def get_async(
        self,
        session: AsyncSession,
        stmt: Select,
        page_number: int,
    ) -> CountOffsetPage:

        total_items = (await session.execute(
            select(count()).select_from(stmt)
        )).scalar_one()
        stmt = stmt.limit(self.limit)
        stmt = stmt.offset((page_number - 1) * self.limit)
        items = (await session.execute(stmt)).scalars()
        return self.prepare_page_instance(page_number, total_items, items)

    def get_sync(
        self,
        session: Session,
        stmt: Select,
        page_number: int,
    ) -> CountOffsetPage:
        total_items = session.execute(
            select(count()).select_from(stmt)
        ).scalar_one()
        stmt = stmt.limit(self.limit)
        stmt = stmt.offset((page_number - 1) * self.limit)
        items = session.execute(stmt).scalars()
        return self.prepare_page_instance(page_number, total_items, items)

    def prepare_page_instance(
        self,
        page_number: int,
        total_items: int,
        items: AsyncScalarResult,
    ) -> CountOffsetPage:
        previous_page_number = None
        if page_number > 1:
            previous_page_number = page_number - 1

        next_page_number = None
        if page_number * self.limit < total_items:
            next_page_number = page_number + 1

        return CountOffsetPage(
            items=items,
            next=next_page_number,
            previous=previous_page_number,
            total_items=total_items,
        )
