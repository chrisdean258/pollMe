#!/usr/bin/python3

import pymysql as PyMySQL
import dbconn
# Open database connection
db = dbconn.dbcon()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM rooms"
# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
#print(results)
for row in results:
   fname = row[0]
   lname = row[1]
   age = row[2]
   # Now print fetched result
   print ("fname = %s,lname = %s,age = %s" % \
          (fname, lname, age ))

# disconnect from server
db.close()

