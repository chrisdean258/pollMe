#!/usr/bin/python
import MySQLdb

def dbcon():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")        # name of the data base
	TEST ADATA FOR NO PUSH
	return db
