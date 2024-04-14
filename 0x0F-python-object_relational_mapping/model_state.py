#!/usr/bin/python3
"""
Contains class state and base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metaData=mymetadata)


class State(Base):
    """
    CLASS with ID and NAME attribute of each state
    """
    __table__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
