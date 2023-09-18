from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SomeClass(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True)
    name = Column(String(50))(


table = SomeClass

