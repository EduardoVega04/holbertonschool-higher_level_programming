#!/usr/bin/python3
"""Contains the class definition of a State
 and an instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """The class"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement='auto'
    )
    name = Column(
        String(128),
        nullable=False
    )
