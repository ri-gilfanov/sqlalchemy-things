import sqlalchemy as sa
from sqlalchemy import create_engine, orm
from sqlalchemy.orm.session import Session

metadata = sa.MetaData()
base_model = orm.declarative_base(metadata=metadata)
engine = create_engine('sqlite+aiosqlite:///')
session = Session()
base_model.metadata.create_all(engine)
