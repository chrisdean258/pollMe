#!/usr/bin/python3

import pymysql as PyMySQL
import dbconn
import random
import datetime

db = dbconn.dbcon()

tempTime = datetime.datetime.now()
curDate = tempTime.strftime("%Y-%m-%d")
curTime = tempTime.strftime("%H:%M:%S")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#Kelsey
	#Phone Number
	#Full Name

#Gen Code

#Insert into mysql

#Text code to Phone Number

def fromPage(phoneNumber, fullName):
	phoneNumber = phoneNumber
	fullName = fullName
	genCode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))

	print(genCode)

	sql = """INSERT INTO reg(name, phoneNumber, regDate, regTime, regCode, regConf, classes) VALUES ('"""+ fullName  +"""', '""" + phoneNumber  +"""', '""" + curDate  +"""', '"""+ curTime  +"""', '"""+ genCode +"""', 'n', 'utk102')"""
	
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	db.close()	
		
def main():
	phoneNumber = "0001111234"
	fullName = "Test Name"

	fromPage(phoneNumber, fullName)

if __name__ == "__main__":
    main()




