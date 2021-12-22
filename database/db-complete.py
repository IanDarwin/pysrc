#!/usr/bin/env python

import os

""" all in one - create a table, populate it, query it, drop it."""

# for PostgreSQL
# from psycopg import connect
# connString = "dbname=test user=test password=fred host=server"

# for SQLite
from sqlite3.dbapi2 import connect
connString = ":memory:" # or a local file name

conn = connect(connString)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE test(
                  id integer primary key,
                  name char(8),
                  value float)""")

cursor.execute("INSERT INTO test(id,name,value) VALUES(1001, 'Hammy', 1.0)")
cursor.execute("INSERT INTO test(id,name,value) VALUES(1002, 'Spammy', 2.0)")

conn.commit()

cursor.execute("select * from test where name like '%y'");

results = cursor.fetchall()
for row in results:
	print("Row:", "id", row[0], "name", row[1], "value", row[2])
print("(expected two rows)")
