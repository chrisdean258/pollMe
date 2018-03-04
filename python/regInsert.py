#!/usr/bin/python3

import pymysql as PyMySQL
import dbconn
import random
import datetime
import textMessage

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
		return "Error with insert"

	db.close()
	return None


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
		return "Error with insert"

	db.close()
	return None

def main():
    pass
	#phoneNumber = "TESTNUMBER HERE"
	#fullName = "TESTNAME"
	#verCode = "TESTVERCODE"

	#fromCode(phoneNumber, verCode)
	#fromPage(phoneNumber, fullName)

if __name__ == "__main__":
    main()




