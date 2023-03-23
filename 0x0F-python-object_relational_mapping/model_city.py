#!/usr/bin/python3
"""Defines a class City"""

from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from model_state import Base


class City(Base):
    """ A city model that defines table cities

        __tablename__ (str): The name of the MySQL table to store Cities.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id(sqlalchemy.Integer): Foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
