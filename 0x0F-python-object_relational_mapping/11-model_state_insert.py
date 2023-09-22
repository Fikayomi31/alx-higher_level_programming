#!/usr/bin/python3
"""This script adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""
from model_state import State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()
    print(new_state.id)
