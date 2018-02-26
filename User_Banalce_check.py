#!/usr/local/bin/python
# python executable
import mysql.connector
import sys
import smtplib

# Send the mail Funktion
def mail():
  SERVER = "smtp.bredband.net"
  FROM = "noreply@skydivesyd.se"
  TO = ?
  message = ?
  server = smtplib.SMTP(SERVER)
  server.sendmail(FROM, TO, message)
  server.quit()

#SQL select function
def sql.skywinsyd():
  from mysql.connector import (connection)
  try:
    cnx = connection.MySQLConnection(user='pyuser', password='py123456',
                                  host='127.0.0.1',
                                  database='skywinsyd')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()
#SQL query
query = ("SELECT InternalNo,MemberNo,FirstName,Emailaddress,Balance,Club,VerifiedLicense from skywinsyd.member WHERE Club = 'SYD' AND VerifiedLicense = 'Y' AND Balance < '0'; ")
    

#SQL select from Portal Database function
def sql.sydportal()
  from mysql.connector import (connection)
  try:
    cnx = connection.MySQLConnection(user='pyuser', password='py123456',
                                  host='127.0.0.1',
                                  database='sydportal')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()

#Check if mail was sent before to user funktion
def prev_check():
  

#Code
cursor.execute(query)
row = cursor.fetchone()
while row is not None:
  if
#If flag exits exit
  else:
    # Send mail and set flag
