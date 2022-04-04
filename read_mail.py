#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
 
import imaplib
from keys_in_mail import login, password
import email


mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login(login, password)
 
mail.list()
mail.select("inbox")

result, data = mail.search(None, "ALL")
 
ids = data[0]

id_list = ids.split()
try:
    latest_email_id = id_list[-1]
except IndexError:
    print("Писем нет!")
else:
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    
    email_message = email.message_from_string(raw_email_string)
     
    print(email_message['To'])
    print(email.utils.parseaddr(email_message['From']))
    print(email_message['Date'])
    print(email_message['Subject'])
    print(email_message['Message-Id'])
    
    
    email_message = email.message_from_string(raw_email_string)
     
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')
            print(body)
    else:    
        body = email_message.get_payload(decode=True).decode('utf-8')
        print(body)