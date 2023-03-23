#!/usr/bin/python3
"""a script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all the tables associated with the Base metadata
    Base.metadata.create_all(engine)

    # Create a new Session instance and bind it to the engine created above
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adds new state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)
