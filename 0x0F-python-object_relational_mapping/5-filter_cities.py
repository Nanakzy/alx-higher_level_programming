#!/usr/bin/python3
"""Lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    # Use triple quotes for multi-line string
    query = """SELECT cities.id, cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s ORDER BY cities.id"""

    state_name = sys.argv[4]

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()
