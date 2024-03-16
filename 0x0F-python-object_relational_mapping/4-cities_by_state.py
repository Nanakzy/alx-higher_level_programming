#!/usr/bin/python3
"""Lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    # Use a single execute statement to fetch and print results
    cursor.execute("SELECT * FROM cities ORDER BY id")
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()
