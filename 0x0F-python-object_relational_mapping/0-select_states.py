#!/usr/bin/python3
"""
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argc[4]

    db = MySQLdb.connect(host="localhost", user=username,
                        password=password, database=database, port=3306)
    cursor = db.cursor()
    curson.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    cursor.close()
    db.close
    for result in results:
        print(result)
