#!/usr/bin/env python

# all in one - create a table, populate it, query it, drop it.

import pathlib
from sqlite3 import connect

file_name = "fred.sqlite"

conn = connect(file_name)
print(conn)

cursor = conn.cursor()
print(cursor)

cursor.execute("DROP TABLE if exists list")

cursor.execute("""CREATE TABLE list(
				id integer primary key,
                  name char(8),
                  email float)""")

cursor.execute("INSERT INTO list(id,name,email) VALUES(1001, 'Hammy', 'ham@spam.com')")
cursor.execute("INSERT INTO list(id,name,email) VALUES(1002, 'Spammy', 'spam@ham.com')")

conn.commit()

cursor.execute("select id,name,email from list where name like '%y'")
results = cursor.fetchall()
for row in results:
        print("Row:", "id", row[0],
			"name", row[1], "email", row[2])

print("All done with DB")
conn.close()
pathlib.Path(file_name).unlink()
