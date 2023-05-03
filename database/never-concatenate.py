#!/usr/bin/env python3

# If you don't know why this is here, see https://xkcd.com/327/
# Meanwhile, DO NOT DO THIS in production!
# A too-common vulnerability in web (and interactive) apps is
# the "SQL Injection" vuln - if the user input is not
# sanitized to remove strings like ' ; -- then the
# attacker can enter a string like 
# "'; drop table students; --"
# and if the stars align in their favor, you lose big time!
# And maybe get your organization name on the front page
# of the business section - as an IT or even business failure.

sql_template = "select * from students where name = '{}'"

while True:
	name = input("Enter student login name: ")
	sql_command = sql_template.format(name);
	print(sql_command)
	if sql_command.find("';") > 0:
		print("Saved ya from gettin' pwned, pardner!");
	else:
		print("What a nice name! I will go fetch your record");
		# ... goes ahead and does the query here ...
