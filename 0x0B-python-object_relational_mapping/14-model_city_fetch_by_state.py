#!/usr/bin/python3
"""Cities in State"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from model_city import City


def fetch_cities():
    """prints all City objects from the database hbtn_0e_14_usa"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    c_query = session.query(State, City).order_by(City.id).filter(City.state_id == State.id).all()

    for state, city in c_query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities()
