#!/usr/bin/python3

import pymysql as PyMySQL
from . import dbconn
import datetime

def askQuestion(phoneNumber, roomCode, message):
	db = dbconn.dbcon()

	tempTime = datetime.datetime.now()
	curDate = tempTime.strftime("%Y-%m-%d")
	curTime = tempTime.strftime("%H:%M:%S")

	cursor = db.cursor()
	phoneNumber = phoneNumber
	roomCode = roomCode
	message = message

	sql = """INSERT INTO ans(ansDate, ansTime, roomId, phone, message, ansClassId) VALUES ('"""+ curDate +"""', '"""+ curTime +"""', '"""+ roomCode +"""','"""+ phoneNumber +"""','"""+ message +"""','N/A')"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		return "Insert had an error"

	db.close()
	return None

def getQuestionsRoom(roomCode):
	db = dbconn.dbcon()
	cursor = db.cursor()
	roomCode = roomCode

	sql = """SELECT * FROM ans WHERE roomId='"""+ roomCode+"""'"""
	cursor.execute(sql)

	results = cursor.fetchall()
	return results


def main():
	#roomCode="123456"
	#getQuestionsRoom(roomCode)
	pass
	#phoneNumber = "8970987890"
	#roomCode = "testCode"
	#message = "TEST MESSAGE"

	#askQuestion(phoneNumber, roomCode, message)

if __name__ == "__main__":
    main()




