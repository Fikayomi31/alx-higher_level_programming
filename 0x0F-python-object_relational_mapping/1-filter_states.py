#!/usr/bin/python3
"""
Script that list all states with a name starting with
N from the daatabase
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY `id` ASC")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
