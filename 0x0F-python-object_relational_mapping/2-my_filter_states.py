#!/usr/bin/python3
"""
Script that takes in an argument and display
all values in the table to match the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    find_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
                    ORDER BY states.id ASC".format(find_state))
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
