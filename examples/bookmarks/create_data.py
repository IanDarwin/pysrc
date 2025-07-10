#!/usr/bin/env python3

# create and populate the database.

# for SQLite
from sqlite3.dbapi2 import connect
connString = "bookmarks.db"

# for PostgreSQL
# from psycopg2 import connect
# connString = "dbname=test user=test password=fred host=server"

sql_create_topics = "CREATE TABLE IF NOT EXISTS topics(id character varying(32) not null, description character varying);"

sql_create_bookmarks = """
	CREATE TABLE IF NOT EXISTS bookmark(
		id bigint integer primary key,
		owner integer default 1,
		url character varying not null unique,
		text character varying not null,
		topic_id character varying not null references topic(id)
	);"""

sql_topic = 'py' # used as pkey and fkey

with connect(connString) as conn:
	cur = conn.cursor();

	cur.execute(sql_create_topics)
	cur.execute(f"INSERT INTO topics(id,description) VALUES('{sql_topic}', 'Python Language and Applications')")
	cur.execute(sql_create_bookmarks)

	filename = "/home/ian/lt1906/teachnotes.txt"
	try:
		ifile = open(filename)
	except FileNotFoundError:
		print('Failed to open', filename)
	else:
		with ifile:
			for line in ifile:
				if line.startswith("https:"):
					s = line[:-1].split(' ', 1);
					if len(s) != 2:
						raise Exception("Wrong number of fields on " + line);
					url = s[0]
					text = s[1]
					try:
						sql = f"INSERT INTO bookmark(topic_id, url, text) VALUES('{sql_topic}', '{url}', '{text}');"
						print("Trying", sql)
						cur.execute(sql);
					except Exception as ex:
						print("Insert failed:", ex)
print("Insertions All Done")
