#!/usr/local/bin/python
# python executable
import mysql.connector
#import smtplib

query = ("SELECT InternalNo,MemberNo,FirstName,Emailaddress,Balance,Club,VerifiedLicense from skywinsyd.member WHERE Club = 'SYD' AND VerifiedLicense = 'Y' AND Balance < '0'; ")

#Mail Config
#SERVER = "smtp.bredband.net"
#FROM = "noreply@skydivesyd.se"

#SQL config
from mysql.connector import (connection)
try:
cnx = connection.MySQLConnection(user='pyuser', password='py123456',
host='127.0.0.1',
database='skywinsyd')

cur = cnx.cursor()
cur.execute(query)

for FirstName, Emailaddress in cur.fetchall() :
    print FirstName, Emailaddress

except mysql.connector.Error as err:
if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
print("Something is wrong with your user name or password")
elif err.errno == errorcode.ER_BAD_DB_ERROR:
print("Database does not exist")
else:
print(err)
else:

#??

# Send the mail
#server = smtplib.SMTP(SERVER)
#server.sendmail(FROM, TO, message)
#server.quit()

cnx.close()  