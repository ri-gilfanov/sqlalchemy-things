from typing import Optional, Union

from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncScalarResult, AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select, select
from sqlalchemy.sql.functions import count


class OffsetPage:
    next: Optional[int] = None
    previous: Optional[int] = None
    total_items: int = 0

    def __init__(
        self,
        items: Union[AsyncScalarResult, ScalarResult],
        page_number: int,
        page_size: int,
        total_items: int,
    ):
        self.items = items
        self.page_size = page_size
        self.total_items = total_items

        if page_number * self.page_size < self.total_items:
            self.next = page_number + 1

        if page_number > 1:
            self.previous = page_number - 1

    @property
    def last(self) -> int:
        return self.total_items // self.page_size + bool(
            self.total_items % self.page_size)


class OffsetPaginator:
    items: Union[AsyncScalarResult, ScalarResult]
    page_number: int
    total_items: int

    def __init__(self, page_size: int = 10, max_page: Optional[int] = None):
        self.page_size = page_size
        self.max_page = max_page

    async def get_page_async(
        self,
        session: AsyncSession,
        stmt: Select,
        page_number: int,
    ) -> OffsetPage:
        stmt = self.handle_max_page(stmt, page_number)
        total_items = (await session.execute(
            select(count()).select_from(stmt.subquery())
        )).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((page_number - 1) * self.page_size)

        items = (await session.execute(stmt)).scalars()
        return OffsetPage(items, page_number, self.page_size, total_items)

    def get_page_sync(
        self,
        session: Session,
        stmt: Select,
        page_number: int,
    ) -> OffsetPage:
        stmt = self.handle_max_page(stmt, page_number)
        total_items = session.execute(
            select(count()).select_from(stmt.subquery())
        ).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((page_number - 1) * self.page_size)

        items = session.execute(stmt).scalars()
        return OffsetPage(items, page_number, self.page_size, total_items)

    def handle_max_page(
        self,
        stmt: Select,
        page_number: int,
    ) -> Select:
        if self.max_page:
            if page_number > self.max_page:
                raise ValueError

            if self.max_page:
                stmt = stmt.limit(self.max_page * self.page_size)

        return stmt
