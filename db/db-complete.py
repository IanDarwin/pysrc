#!/usr/bin/env python

# all in one - create a table, populate it, query it, drop it.

from psycopg import connect;

conn = connect("dbname=test user=test password=fred host=localhost")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE list(
                  name char(8),
                  value float)""")
cursor.execute("INSERT INTO list VALUES ('one', 1.0)")
cursor.execute("INSERT INTO list VALUES ('two', 2.0)")
conn.commit()

cursor.execute("select * from list where name like 'o%'");
results = cursor.fetchall()
for i in range(len(results)):
	row = results[i]
	print "Row", i, "name", row[0], "value", row[1]

