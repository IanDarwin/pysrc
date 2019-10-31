''' Send a short email via SMTP to a mail server '''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Collect parameters - you usually need an account on the server to send mail
sender_email="user@domain.com"			# changeme
sender_name="user"						# may be same as sender_email, or just name part
send_host="mail.domain.com"			# changeme
port=587							# submission service
passwd="SOME_PASSWD"				# changeme
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
message="Welcome to the world of email from Python"
msg.attach(MIMEText(message, 'plain'))

print("Sending your message")
s.send_message(msg)

print("All Done.")
