#!/usr/bin/env python2
# coding=utf-8

import os
import re
import sys
import time
import curl
import shutil
import threading
from datetime import datetime
from commands import getstatusoutput as c

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

test_user = 'Test'
mail_recipients = ['test@fsksyd.se']


def send_mail(send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    server = 'smtp.XXX.se'
    port   = '25'
    send_from = test_user + "@fsksyd.se"
#    msg = MIMEMultipart()
    msg = MIMEMultipart('alternative')
    msg['From'] = send_from[:send_from.find('@')].replace('.', ' ').upper() + " <" + send_from + ">"
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

#    msg.attach(MIMEText(text))
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(text, 'html'))
    smtp = smtplib.SMTP(server, port)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

send_mail(mail_recipients, "Subject", "Body")