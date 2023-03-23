#!/usr/bin/python3
""" a script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Creates all tables associated with the metadata
    Base.metadata.create_all(engine)

    # Creates a session and binds it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object to delete it's specified attribute
    states_to_delete = session.query(State).filter(State.name
                                                   .like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
