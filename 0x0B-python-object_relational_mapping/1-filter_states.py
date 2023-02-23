#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def filter_states():
    """Takes 3 arguments to get query"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
