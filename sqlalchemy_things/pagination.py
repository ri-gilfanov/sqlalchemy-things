from typing import Any, List, Optional, Union

from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncScalarResult, AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select, select
from sqlalchemy.sql.functions import count

Result = Union[AsyncScalarResult, ScalarResult]


class OffsetPage:
    next: Optional[int] = None
    previous: Optional[int] = None

    def __init__(
        self,
        items: List[Any],
        number: int,
        page_size: int,
        total: int,
    ):
        self.items = items
        self.page_size = page_size
        self.total = total

        if number * self.page_size < self.total:
            self.next = number + 1

        if number > 1 and len(items) > 0:
            self.previous = number - 1

    @property
    def last(self) -> int:
        return self.total // self.page_size + bool(
            self.total % self.page_size)


class OffsetPaginator:
    number: int
    total: int

    def __init__(self, page_size: int = 20, max_page: Optional[int] = None):
        self.page_size = page_size
        self.max_page = max_page

    async def get_page_async(
        self,
        session: AsyncSession,
        stmt: Select,
        number: int,
    ) -> Optional[OffsetPage]:
        stmt = self.handle_page_number(stmt, number)
        if stmt is None:
            return None
        total = (await session.execute(
            select(count()).select_from(stmt.subquery())
        )).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((number - 1) * self.page_size)

        items: List[Any] = list((await session.execute(stmt)).scalars())
        return OffsetPage(items, number, self.page_size, total)

    def get_page_sync(
        self,
        session: Session,
        stmt: Select,
        number: int,
    ) -> Optional[OffsetPage]:
        stmt = self.handle_page_number(stmt, number)
        if stmt is None:
            return None
        total = session.execute(
            select(count()).select_from(stmt.subquery())
        ).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((number - 1) * self.page_size)

        items = list(session.execute(stmt).scalars())
        return OffsetPage(items, number, self.page_size, total)

    def handle_page_number(self, stmt: Select, number: int) -> Optional[Select]:
        if self.max_page:
            if number < 1:
                return None
            if number > self.max_page:
                return None

            stmt = stmt.limit(self.max_page * self.page_size)

        return stmt
