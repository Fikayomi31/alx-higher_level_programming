#!/usr/bin/python3
"""Script that list all cities from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    WHERE cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
