import cx_Oracle

conn = cx_Oracle.connect("some_db_account", "some_db_passwd", "oracledb123");
print("Database version:", conn.version)

cursor = conn.cursor()

cursor.execute("select * from test where first_name = 'Ian'");

for row in cursor.fetchall():
	print(row)

