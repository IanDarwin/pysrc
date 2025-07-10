#!/usr/bin/env python3

# create and populate the database.
# The SQL is complicated by the need to be idempotent since
# we update the text file from time to time and want to
# "sync" that into the database when it changes.

# for SQLite
from sqlite3.dbapi2 import connect
connString = "bookmarks.db"

# for PostgreSQL
# from psycopg2 import connect
# connString = "dbname=test user=test password=fred host=server"

# input file
filename = "/home/ian/lt1906/teachnotes.txt"

# Table creation
sql_create_topics = ("CREATE TABLE IF NOT EXISTS topic("
		"id character varying(32) not null unique, description character varying);")
sql_create_bookmarks = """
	CREATE TABLE IF NOT EXISTS bookmark(
		id bigint integer primary key,
		owner integer default 1,
		url character varying not null unique,
		text character varying not null,
		topic_id character varying not null references topic(id)
	);"""

sql_topic = 'py' # used as pkey in topics, and fkey in bookmark

with connect(connString) as conn:
	cur = conn.cursor()

	cur.execute(sql_create_topics)
	cur.execute(f"INSERT INTO topic(id,description) VALUES('{sql_topic}',"
				f"'Python Language, Frameworks, and Applications') on conflict do nothing;")
	cur.execute(sql_create_bookmarks)

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
						cur.execute(sql);
					except Exception as ex:
						print("Insert failed:", ex)
print("Insertions All Done")
