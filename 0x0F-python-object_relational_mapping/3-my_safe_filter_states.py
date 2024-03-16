#!/usr/bin/python3
"""Displays all values in the states table and is safe from MySQL Injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))  # Pass state_name as a tuple

    # Fetch all matching rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
