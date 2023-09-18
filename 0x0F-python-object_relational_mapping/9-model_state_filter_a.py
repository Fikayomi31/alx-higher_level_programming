#!/usr/bin/python3
"""script that lists all State objects that contain the
letter a from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name.contains('a'))

    if state is not None:
        for stat in state:
            print("{}: {:s}".format(stat.id, stat.name))
