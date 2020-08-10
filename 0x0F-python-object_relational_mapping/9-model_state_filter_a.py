#!/usr/bin/python3
"""Script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    req = session.query(State).order_by(State.id)
    for i, state in enumerate(req, 1):
        if 'a' in state.name:
            print("{}: {}".format(i, state.name))

    session.close()
