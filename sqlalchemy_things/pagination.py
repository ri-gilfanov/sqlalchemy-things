from typing import Optional, Union

from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncScalarResult, AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select, select
from sqlalchemy.sql.functions import count


class OffsetPaginator:
    items: Union[AsyncScalarResult, ScalarResult]
    page_number: int
    total_items: int

    def __init__(self, page_size: int = 10, max_page: Optional[int] = None):
        self.page_size = page_size
        self.max_page = max_page

    async def prepare_page_async(
        self,
        session: AsyncSession,
        stmt: Select,
        page_number: int,
    ) -> None:
        self.page_number = page_number
        stmt = self.handle_max_page(stmt)
        self.total_items = (await session.execute(
            select(count()).select_from(stmt.subquery())
        )).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((page_number - 1) * self.page_size)
        self.items = (await session.execute(stmt)).scalars()

    def prepare_page_sync(
        self,
        session: Session,
        stmt: Select,
        page_number: int,
    ) -> None:
        self.page_number = page_number
        stmt = self.handle_max_page(stmt)
        self.total_items = session.execute(
            select(count()).select_from(stmt.subquery())
        ).scalar_one()

        stmt = stmt.limit(self.page_size)
        stmt = stmt.offset((page_number - 1) * self.page_size)
        self.items = session.execute(stmt).scalars()

    def handle_max_page(
        self,
        stmt: Select,
    ) -> Select:
        if self.max_page:
            if self.page_number > self.max_page:
                raise ValueError

            if self.max_page:
                stmt = stmt.limit(self.max_page * self.page_size)

        return stmt

    def get_items(self) -> Union[AsyncScalarResult, ScalarResult]:
        return self.items

    def get_last_page_number(self) -> int:
        return self.total_items // self.page_size + bool(
            self.total_items % self.page_size)

    def get_next_page_number(self) -> Optional[int]:
        next_number = None
        if self.page_number * self.page_size < self.total_items:
            next_number = self.page_number + 1
        return next_number

    def get_previous_page_number(self) -> Optional[int]:
        previous_number = None
        if self.page_number > 1:
            previous_number = self.page_number - 1
        return previous_number
