#!/usr/bin/python3
"""
Script take all argument and display value
and safe from injestion
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s\
                    ORDER BY states.id ASC", {'name': state})
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
