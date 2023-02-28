#!/usr/bin/python3
"""All cities by state function"""
import MySQLdb
from sys import argv


def all_cities_by_state():
    """Takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id", (argv[4], ))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row[0] + ",")
    cur.close()
    db.close()


if __name__ == "__main__":
    all_cities_by_state()
