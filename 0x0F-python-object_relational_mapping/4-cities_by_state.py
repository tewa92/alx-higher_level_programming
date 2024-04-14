#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access to the db get list of the states from db
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute(""" SELECT cities.id,
                cities.name,
                states.id=cities.states_id """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
