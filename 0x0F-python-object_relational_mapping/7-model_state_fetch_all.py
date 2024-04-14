#!/usr/bin/python3
"""
Start LINK class to table in db
"""
import sys
from model_state import Base, state
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(state).order_by(state.id):
        print(instance.id, instance.name, sep=': ')
