import pytest
import sqlalchemy as sa

from sqlalchemy_things.declarative import (
    BigIntegerPrimaryKeyMixin,
    CascadeBigIntegerPrimaryKeyMixin,
    CascadeIntegerPrimaryKeyMixin,
    CascadeUUIDPrimaryKeyMixin,
    IntegerPrimaryKeyMixin,
    PolymorphicMixin,
    UUIDPrimaryKeyMixin,
)


@pytest.mark.asyncio
async def test_single_table_with_big_integer_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(base_model, BigIntegerPrimaryKeyMixin, PolymorphicMixin):
        __tablename__ = 'single_table'

    class ChildA(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field_a = sa.Column(sa.String(255))

    class ChildB(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field_b = sa.Column(sa.String(255))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(pk=1, field_a='a' * 255),
            ChildB(pk=2, field_b='a' * 127),
        ])


@pytest.mark.asyncio
async def test_single_table_with_integer_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(base_model, IntegerPrimaryKeyMixin, PolymorphicMixin):
        __tablename__ = 'single_table'

    class ChildA(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field_a = sa.Column(sa.String(255))

    class ChildB(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field_b = sa.Column(sa.String(127))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(field_a='a' * 255),
            ChildB(field_b='a' * 127),
        ])


@pytest.mark.asyncio
async def test_single_table_with_uuid_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(base_model, UUIDPrimaryKeyMixin, PolymorphicMixin):
        __tablename__ = 'single_table'

    class ChildA(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field_a = sa.Column(sa.String(255))

    class ChildB(Parent):
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field_b = sa.Column(sa.String(255))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(field_a='a' * 255),
            ChildB(field_b='a' * 127),
        ])


@pytest.mark.asyncio
async def test_joined_table_with_big_integer_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(
        base_model,
        CascadeBigIntegerPrimaryKeyMixin,
        PolymorphicMixin,
    ):
        __tablename__ = 'parent_table'

    class ChildA(Parent):
        __tablename__ = 'child_table_1'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __tablename__ = 'child_table_2'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field = sa.Column(sa.String(127))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(pk=1, field='a' * 255),
            ChildB(pk=2, field='a' * 127),
        ])


@pytest.mark.asyncio
async def test_joined_table_with_integer_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(base_model, CascadeIntegerPrimaryKeyMixin, PolymorphicMixin):
        __tablename__ = 'parent_table'

    class ChildA(Parent):
        __tablename__ = 'child_table_1'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __tablename__ = 'child_table_2'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field = sa.Column(sa.String(127))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(field='a' * 255),
            ChildB(field='a' * 127),
        ])


@pytest.mark.asyncio
async def test_test_joined_table_with_uuid_pk(
    base_model,
    sqlite_engine,
    sqlite_session,
):
    class Parent(base_model, CascadeUUIDPrimaryKeyMixin, PolymorphicMixin):
        __tablename__ = 'parent_table'

    class ChildA(Parent):
        __tablename__ = 'child_table_1'
        __mapper_args__ = {'polymorphic_identity': 'child_a'}
        field = sa.Column(sa.String(255))

    class ChildB(Parent):
        __tablename__ = 'child_table_2'
        __mapper_args__ = {'polymorphic_identity': 'child_b'}
        field = sa.Column(sa.String(127))

    async with sqlite_engine.begin() as conn:
        await conn.run_sync(base_model.metadata.create_all)

    async with sqlite_session.begin():
        sqlite_session.add_all([
            ChildA(field='a' * 255),
            ChildB(field='a' * 127),
        ])
