#!/usr/bin/python3
"""Delete states"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


def delete_state():
    """Cdeletes all State objects with a name containing the letter a from the
    database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State)
    for row in state:
        if '%a%' in row.name:
            session.delete(row)

    session.commit()
    session.close()


if __name__ == "__main__":
    delete_state()
