from typing import Optional, Union

from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncScalarResult, AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select, select
from sqlalchemy.sql.functions import count


class OffsetPage:
    def __init__(
        self,
        items: Union[AsyncScalarResult, ScalarResult],
        next_number: Optional[int],
        previous_number: Optional[int],
        total_items: int,
    ):
        self.items = items
        self.next_number = next_number
        self.previous_number = previous_number
        self.total_items = total_items


class OffsetPaginator:
    def __init__(self, page_size: int = 10, max_page: Optional[int] = None):
        self.page_size = page_size
        self.max_page = max_page

    async def get_page_async(
        self,
        session: AsyncSession,
        stmt: Select,
        page_number: int,
    ) -> OffsetPage:
        stmt = self.handle_max_page_attribute(stmt, page_number)
        total_items = (await session.execute(
            select(count()).select_from(stmt.subquery())
        )).scalar_one()

        stmt = stmt.limit(self.page_size).offset((page_number - 1) * self.page_size)
        items = (await session.execute(stmt)).scalars()

        return self.prepare_page_instance(page_number, total_items, items)

    def get_page_sync(
        self,
        session: Session,
        stmt: Select,
        page_number: int,
    ) -> OffsetPage:
        stmt = self.handle_max_page_attribute(stmt, page_number)
        total_items = session.execute(
            select(count()).select_from(stmt.subquery())
        ).scalar_one()

        stmt = stmt.limit(self.page_size).offset((page_number - 1) * self.page_size)
        items = session.execute(stmt).scalars()

        return self.prepare_page_instance(page_number, total_items, items)

    def handle_max_page_attribute(self, stmt, page_number) -> Select:
        if self.max_page:
            if page_number > self.max_page:
                raise ValueError

            if self.max_page:
                stmt = stmt.limit(self.max_page * self.page_size)

        return stmt

    def prepare_page_instance(
        self,
        page_number: int,
        total_items: int,
        items: AsyncScalarResult,
    ) -> OffsetPage:
        previous_number = None
        if page_number > 1:
            previous_number = page_number - 1

        next_number = None
        if page_number * self.page_size < total_items:
            next_number = page_number + 1

        return OffsetPage(
            items=items,
            next_number=next_number,
            previous_number=previous_number,
            total_items=total_items,
        )
