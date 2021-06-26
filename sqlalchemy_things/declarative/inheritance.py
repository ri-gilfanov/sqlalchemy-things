import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_things.declarative import DeclarativeMixin


@orm.declarative_mixin
class PolymorphicMixin(DeclarativeMixin):
    definition = sa.Column(sa.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': definition,
    }
