# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import (Column, String)


class GeokretyType(Base):
    __tablename__ = 'gk-geokrety-types'

    id = Column(
        'id',
        String(1),
        primary_key=True,
        key='id',
    )

    name = Column(
        'name',
        String(75),
        key='name',
        nullable=False,
    )
