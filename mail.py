import smtplib

SERVER = "smtp.bredband.net"

FROM = "noreply@skydivesyd.se"
TO = ["test1@skydivesyd.se"] 

SUBJECT = "test"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()