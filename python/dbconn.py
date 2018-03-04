#!/usr/bin/python
import MySQLdb

#this is a test comment that should not be added

def dbcon():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")        # name of the data base
	return db
