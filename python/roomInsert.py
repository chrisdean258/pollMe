#!/usr/bin/python3

import pymysql as PyMySQL
from . import dbconn
import datetime
import random

def createRoom(question):
	db = dbconn.dbcon()

	tempTime = datetime.datetime.now()
	curDate = tempTime.strftime("%Y-%m-%d")
	curTime = tempTime.strftime("%H:%M:%S")
	cursor = db.cursor()
	genCode = ''.join(random.choice('0123456789ABCDEF') for i in range(6))

	sql = """INSERT INTO rooms(roomId, classId, userCreated, roomDate, roomTime, question) VALUES ('"""+genCode+"""','N/A','N/A','"""+curDate+"""','"""+curTime+"""','"""+question+"""')"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		return "Insert had an error"

	db.close()
	return genCode

def getQuestion(roomId):
	db = dbconn.dbcon()
	cursor = db.cursor()

	sql = """SELECT question FROM rooms WHERE roomId='"""+roomId+"""'"""
	cursor.execute(sql)

	results = cursor.fetchall()
	return results

def main():
	#roomCode="123456"
	#getQuestionsRoom(roomCode)	
	#question = "This is a question"
	#createRoom(question)
	pass
	#phoneNumber = "8970987890"
	#roomCode = "testCode"
	#message = "TEST MESSAGE"

	#askQuestion(phoneNumber, roomCode, message)

if __name__ == "__main__":
    main()




