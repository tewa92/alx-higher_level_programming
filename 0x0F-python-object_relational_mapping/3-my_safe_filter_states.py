#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa

Now the script is safe from MySQL injection
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
    match = sys.argv[4]
    cur.excute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
