#!/usr/bin/python3
"""
Print the state name from db if they contain letter 'a' inside the name
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_enggine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_enggine('mysql+mysqlb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_All(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    for instance in Session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
