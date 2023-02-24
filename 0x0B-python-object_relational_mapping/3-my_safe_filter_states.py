#!/usr/bin/python3
"""Filter states by user function"""
import MySQLdb
from sys import argv


def my_filter_states():
    """takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
    but is safe from sql injections."""

    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}' ORDER BY id"
                    .format(argv[4]))
        query_rows = cur.fetchall()

        for rows in query_rows:
            print(row)
        cur.close()
        db.close()
    else:
        return

    if __name__ == "__main__":
        my_filter_states()
