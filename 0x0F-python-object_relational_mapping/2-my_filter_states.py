#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_Name = sys.argv[3]
    state_Name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_Name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(state_Name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
