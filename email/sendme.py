''' Send a short email via SMTP to a mail server '''

import smtplib
import email.mime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Collect parameters - you usually need an account on the server to send mail
sender="SOMEBODY@foo.com"			# changeme
send_host="smtp.gmail.com"			# changeme
port=587							# submission service
passwd="SOME_PASSWD"				# changeme
recip="RECIPIENT@SOMEDOMAIN.com"	# changeme

print("Connecting to the SMTP server")
s = smtplib.SMTP(host=send_host, port=587)
s.starttls()

print("Logging you in")
s.login(sender, passwd)

print("Making a message")
msg = multipart.MIMEMultipart()       # new message
msg['From']=sender
msg['To']=recip
msg['Subject']="We can send email from Python"
message="Welcome to the world of email from Python"
msg.attach(MIMEText(message, 'plain'))

print("Sending your message")
s.send_message(msg)

print("All Done.")
