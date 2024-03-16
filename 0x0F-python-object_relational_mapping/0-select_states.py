#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    try:
        #connect to MySQL server
        db = MySQL.connect(host="localhost",
                           port=3306,
                           user=username,
                           pswd=password,
                           db=batadase)

        #create cursor object
        cursor = db.cursor()

        #execute the query to select all states, sorted by states.id ascending order
        cursor.execute("SELECT *FROM states ORDER BY id")

        #fetch all rows from the result set
        states = cursor.fetchall()

        #print results
        for state in states:
            print(state)

        #close the cursor and database connection
        cursor.close()
        db.close()

        #handle errors
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


