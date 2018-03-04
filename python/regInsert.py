#!/usr/bin/python3

import pymysql as PyMySQL
import dbconn
import random
import datetime
import textMessage



# prepare a cursor object using cursor() method

#Kelsey
	#Phone Number
	#Full Name

#Gen Code

#Insert into mysql

#Text code to Phone Number

def fromPage(phoneNumber, fullName):
	db = dbconn.dbcon()

	tempTime = datetime.datetime.now()
	curDate = tempTime.strftime("%Y-%m-%d")
	curTime = tempTime.strftime("%H:%M:%S")
	
	cursor = db.cursor()
	cursor2 = db.cursor()

	phoneNumber = phoneNumber
	fullName = fullName
	genCode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))

	sqlCheck = """SELECT COUNT(id) FROM reg WHERE phoneNumber='"""+ phoneNumber  +"""'"""
	cursor2.execute(sqlCheck)
	numCheck = cursor2.fetchall()
	for row in numCheck:
		numStuff = row[0]

	if numStuff > 1:
		return "Error phone number already registered"

	sql = """INSERT INTO reg(name, phoneNumber, regDate, regTime, regCode, regConf, classes) VALUES ('"""+ fullName  +"""', '""" + phoneNumber  +"""', '""" + curDate  +"""', '"""+ curTime  +"""', '"""+ genCode +"""', 'n', 'utk102')"""
	
	try:
		cursor.execute(sql)
		db.commit()
		phoneNumber = "+1" + phoneNumber
		genCode = genCode + " is your PollMe verification code."
		textMessage.send_text(phoneNumber, genCode)
	except:
		db.rollback()

	db.close()	
	
def fromCode(phoneNumber, verCode):
	db = dbconn.dbcon()

	tempTime = datetime.datetime.now()
	curDate = tempTime.strftime("%Y-%m-%d")
	curTime = tempTime.strftime("%H:%M:%S")
	
	cursor = db.cursor()

	phoneNumber = phoneNumber
	verCode = verCode

	sql = """UPDATE reg SET regConf='y' WHERE phoneNumber='"""+ phoneNumber +"""' AND regCode='"""+ verCode +"""'"""

	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	
	db.close()

def main():
	phoneNumber = "8654940446"#"9319790204"
	fullName = "Chris Dean"
	verCode = '371C7A'

	#fromCode(phoneNumber, verCode)

	fromPage(phoneNumber, fullName)

if __name__ == "__main__":
    main()




