#!/usr/bin/python
# -*- coding: ISO-8859-4 -*-
import regex
from sendgrid_mail import send_mail
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import time

def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
    
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
            return conn
        else:
            print('Connection failed.')
            return None

    except Error as error:
        print(error)

def disconnect(conn):
    try:
        conn.cursor().close()
        conn.close()
        print('Connection closed successfully.')
    except Error as error:
        print(error)

def create_maildata(clean_data, mailset):
    print('Creating maildata...')
    dataset = {}
    for mail in mailset:
        jumplist = []
        for row in clean_data:
            splitted_row = str(row).split(',')
            if mail == splitted_row[12]:
                jumplist.append(row)
        dataset[mail] = jumplist
    print('Done creating maildata.')
    #print(dataset.items())
    return dataset

def create_mailaddr_set(data):
    maillist = []
    print('Creating unique mailset...')
    for row in data:
        splitted_row = str(row).split(',')
        maillist.append(splitted_row[12])
    mailset = set(maillist)
    print('Done creating unique mailset.')
    print('Unique mails found: ', len(mailset))
    return mailset

def cleanup_results(sqlrows):
        cleaned_sql = []
        print('Begin cleaning up sqldata...')
        for row in sqlrows:
            print(row)
            str_row = str(row)
            str_row = str_row.replace("u'", '')
            str_row = str_row.replace("'", '')
            str_row = str_row.replace('(datetime.datetime(', '')
            str_row = str_row.replace('Decimal(', '')
            str_row = str_row.replace(')', '')
            str_row = str_row.replace("\\xf6", 'ö')
            str_row = str_row.replace("\\xd6", 'Ö')
            cleaned_sql.append(str_row)
        print('Done cleaning up sqldata.')
        for row in cleaned_sql:
            print(row)
        return cleaned_sql

def query_with_fetchall(conn):
    try:
        date = '2017-10-06' #TEST
        #date = time.strftime("%Y-%m-%d")
        #print(date)
        print('Fetching jumpdata for date: ', date)
        cursor = conn.cursor()
        cursor.execute("""SELECT `member`.AccountNo, `member`.FirstName, `member`.LastName, `member`.Emailaddress, TransNo, TransType, AccountType, Regdate, Amount, trans.Balance, trans.Comment, PaymentType, trans.LastUpd
                        FROM skywinsyd.trans
                        inner join skywinsyd.`member` on skywinsyd.trans.AccountNo = `member`.AccountNo
                        where trans.Amount < '0' and member.Emailaddress is not null and trans.Regdate > '""" + date + """'
                        order by `member`.Emailaddress asc;""")
        rows = list(cursor.fetchall())
        print('Total Row(s):', len(rows))

        return rows
 
    except Error as e:
        print(e)
        return None

if __name__ == '__main__':
    conn = connect()
    rows = query_with_fetchall(conn)
    disconnect(conn)
    if rows != None:
        clean_data = cleanup_results(rows)
        #mailset = create_mailaddr_set(clean_data)
        #maildata = create_maildata(clean_data, mailset)
        #for mail,value in maildata.items():
            #send_mail(mail,value)
