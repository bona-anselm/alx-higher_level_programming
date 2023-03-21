#!/usr/bin/python3
"""  a script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument. But
    this time, it's safe from MySQL injections!
"""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close
