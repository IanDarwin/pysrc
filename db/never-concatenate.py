#!/usr/bin/env python3

# If you don't know why this is here, see https://xkcd.com/327/
# Meanwhile, DO NOT DO THIS in production!

sql_template = "select * from students where name = '{}'"

while True:
	name = input("Enter student login name: ")
	sql_command = sql_template.format(name);
	print(sql_command)
	if sql_command.find("';") > 0:
		print("Looks like you mighta got pwned, pardner!");
	else:
		print("What a nice name!");
