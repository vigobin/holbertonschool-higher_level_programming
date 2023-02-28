#!/usr/bin/python3
"""Cities by state function"""
import MySQLdb
from sys import argv


def cities_by_state():
    """Lists all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_state()
