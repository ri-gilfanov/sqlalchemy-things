import uuid

import sqlalchemy as sa

from sqlalchemy_things.types import UUIDType


def test_uuid(base_model):
    class Model(base_model):
        __tablename__ = 'table'

        pk = sa.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    Model()
