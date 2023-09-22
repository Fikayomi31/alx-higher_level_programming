#!/usr/bin/python3
"""Script that print state object with the name passed
as argument from the database
"""

import sys
from model_state import State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    s_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == s_name).order_by(
            asc(State.id)).all()
    if not states:
        print('Not found')

    else:
        for state in states:
            print(f'{state.id}')
