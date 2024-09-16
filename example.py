import asyncio

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy_things.declarative import (
    CascadeIntegerPrimaryKeyMixin,
    IntegerPrimaryKeyMixin,
    ParentPrimaryKeyMixin,
    PolymorphicMixin,
)


class Base(orm.DeclarativeBase): ...


# Single table inheritance
class ParentA(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
    __tablename__ = "single_table"


class ChildA1(ParentA):
    __mapper_args__ = {"polymorphic_identity": "child_a1"}
    some_field = sa.Column(sa.String(255))


class ChildA2(ParentA):
    __mapper_args__ = {"polymorphic_identity": "child_a2"}
    other_filed = sa.Column(sa.String(127))


# Joined table inheritance with cascade primary key mixins
class ParentB(Base, CascadeIntegerPrimaryKeyMixin, PolymorphicMixin):
    __tablename__ = "parent_b"


class ChildB1(ParentB):
    __tablename__ = "child_b1"
    __mapper_args__ = {"polymorphic_identity": "child_b1"}
    some_field = sa.Column(sa.String(255))


class ChildB2(ParentB):
    __tablename__ = "child_b2"
    __mapper_args__ = {"polymorphic_identity": "child_b2"}
    some_field = sa.Column(sa.String(127))


# Joined table inheritance with simple primary key mixins
class ParentC(Base, IntegerPrimaryKeyMixin, PolymorphicMixin):
    __tablename__ = "parent_c"


class ChildC1(ParentPrimaryKeyMixin, ParentC):
    __tablename__ = "child_c1"
    __mapper_args__ = {"polymorphic_identity": "child_c1"}
    some_field = sa.Column(sa.String(255))


class ChildC2(ParentPrimaryKeyMixin, ParentC):
    __tablename__ = "child_c2"
    __mapper_args__ = {"polymorphic_identity": "child_c2"}
    some_field = sa.Column(sa.String(127))


async def async_main() -> None:
    engine = create_async_engine("sqlite+aiosqlite://", echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(async_main())
