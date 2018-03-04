#!/usr/bin/python
import MySQLdb
import dbconn

db = dbconn.dbcon()

cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM rooms")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
