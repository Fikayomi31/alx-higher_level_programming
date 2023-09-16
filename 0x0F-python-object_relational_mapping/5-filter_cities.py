#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities\
                    WHERE cities.state.id = (SELECT id FROM states\
                    WHERE name LIKE BINARY %(state_name)s)\
                    ORDER BY cities,id ASC", {'name': state})
    results = cursor.fetchall()
    cursor.close()
    db.close()
    cities = []
    for result in results:
        for city in result:
            cities.append(city)
    print(", ".join(cities))
