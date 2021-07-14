#!/usr/bin/env python3

# If you don't know why this is here, see https://xkcd.com/327/

sql_template = "select * from students where name = '{}'"
name = input("Enter student login name: ")
sql_command = sql_template.format(name);
print(sql_command)
