#!/usr/bin/env python

import os

""" all in one - create a table, populate it, query it, drop it."""

# for PostgreSQL
# from psycopg import connect
# connString = "dbname=test user=test password=fred host=server"

# for SQLite
from sqlite3.dbapi2 import connect
connString = ":memory:" # or a local file name

with connect(connString) as conn:

	cursor = conn.cursor()

	cursor.execute("""CREATE TABLE test(
					  id integer primary key,
					  name char(8),
					  value float)""")

	cursor.execute("INSERT INTO test(id,name,value) VALUES(1001, 'Hammy', 1.0)")
	cursor.execute("INSERT INTO test(id,name,value) VALUES(1002, 'Spammy', 2.0)")

	conn.commit()

	print("Data saved, now retrieving it.");

	cursor.execute("select * from test where name like '%y'");

	for id, name, value in cursor.fetchall():
		print("Row {}, name {}, value {}".format(id, name, value));

	print("(expected two rows)")
