#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py that prints all City
    objects from the database hbtn_0e_14_usaa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State)
    states = query.filter(City.state_id == State.id).order_by(City.id)

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
