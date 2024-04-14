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
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], poet=3306)
    cur = db.cursor()
    cur.excute(""" SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.states_id WHERE states.name=%s""", (sys.argv[4],))

rows = cur.fetchall()
tmp = list(row[0] for row in rows)
print(*tmp, sep=", ")
cur.close()
db.close()
