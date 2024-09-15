import uuid
from typing import Any

import sqlalchemy as sa

from sqlalchemy_things.column_types import UUIDType


def test_uuid(base_model: Any) -> None:
    class Model(base_model):  # type: ignore
        __tablename__ = "table"

        pk = sa.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    Model()
