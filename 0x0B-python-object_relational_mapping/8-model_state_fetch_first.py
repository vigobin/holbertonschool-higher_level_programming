#!/usr/bin/python3
"""First state function"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


def first_state():
    """Prints the first State object from the database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    f_state = session.query(State).first()
    if f_state:
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    first_state()
