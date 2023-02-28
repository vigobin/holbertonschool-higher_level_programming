#!/usr/bin/python3
"""Get a state"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


def get_state():
    """Prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    rows = session.query(State).all()
    for state in rows:
        if state.name == argv[4]:
            print(state.id)
        else:
            print("Not found")

    session.close()


if __name__ == "__main__":
    get_state()
