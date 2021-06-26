import sqlalchemy as sa
import uuid
from sqlalchemy_things.types import UUID


def test_uuid(base_model):
    class Model(base_model):
        __tablename__ = 'table'

        pk = sa.Column(UUID, primary_key=True, default=uuid.uuid4)

    Model()
