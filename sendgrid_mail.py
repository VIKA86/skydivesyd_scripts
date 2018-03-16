#!/usr/bin/python
# -*- coding: ISO-8859-4 -*-
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from datetime import datetime
from sendgrid.helpers.mail import *

def send_mail(mail,data):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("noreplay@skydivesyd.se")
    #to_email = Email(mail)
    #print('email', mail)
    to_email = Email("aad@nocflame.se") #TEST
    print('email', mail)
    subject = "[FSK-SYD] Dagens hoppaktivitet"
    content = Content("text/plain", data)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)