#!/usr/bin/python3
"""This script deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""
from model_state import State
from model_city import City
import sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).filter(
            City.state_id == State.id
    ).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
