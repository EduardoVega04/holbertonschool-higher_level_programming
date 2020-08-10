#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    name = sys.argv[4]
    found = False

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    all_states = session.query(State)

    for state in all_states:
        if state.name == name:
            print("{}".format(state.id))
            found = True
            break

    if found is False:
            print("Not found")

    session.close()
