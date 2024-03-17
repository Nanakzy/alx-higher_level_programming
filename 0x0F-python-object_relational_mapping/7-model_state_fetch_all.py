#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for all State objects
    states = session.query(State).order_by(State.id).all()

    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
