''' Send a short email via SMTP to a mail server '''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Collect parameters - you usually need an account on the server to send mail
sender_email="user@domain.com"			# changeme
sender_name="user"						# may be same as sender_email, or just name part
passwd="SOME_PASSWD"					# changeme
send_host="mail.domain.com"			# changeme
port=587							# submission service
recip="RECIPIENT@SOMEDOMAIN.com"	# changeme

print("Connecting to the SMTP server")
s = smtplib.SMTP(host=send_host, port=587)
print("Starting TLS session")
s.starttls()

print("Logging you in")
s.login(sender_name, passwd)

print("Making a message")
msg = MIMEMultipart()       # new message
msg['From']=sender_email
msg['To']=recip
msg['Subject']="We can send email from Python"
message='''
	<h1>Email from Python</h1>
	Welcome to the brave new world of <a href='https://en.wikipedia.org/wiki/email'>email</a> 
	from <a href="https://python.org/">Python</a>.'''
msg.attach(MIMEText(message, 'html'))

print("Sending your message")
s.send_message(msg)

print("All Done.")
