#! /usr/bin/python
# -*- coding: utf-8 -*-

import httplib2
from xml.dom.minidom import parseString

### VARS
filename = "/var/log/mailcount.log"
logfile = "/var/log/userapps.log"
#https://user:password@mail.google.com/mail/feed/atom
gmail_feed_url = "https://mail.google.com/mail/feed/atom"
users = {
        "<myuser1>@gmail.com":"<mypass1>",
        "<myuser2>@gmail.com":"<mypass2>"
        }
result = []

### FUNC
def ClearFile():
    """ Clears output file. """
    try:
        file = open(filename, 'w')
        try:
            file.write("")
        finally:
            file.close()
    except IOError as strerror:
        WriteLog("[gnm.py/ClearFile] I/O error {0}".format(strerror))

def WriteFile(lines):
    """ Writes new  data to file. """
    try:
        file = open(filename, 'w')
        try:
            for line in lines:
                file.write(line),
                file.write('\n')
        finally:
            file.close()
    except IOError as strerror:
        WriteLog("[gnm.py/WriteFile] I/O error {0}".format(strerror))

def WriteLog(error):
    """ Logs errors to log. """
    try:
        file = open(logfile, 'a')
        try:
            file.write(error + '\n')
        finally:
            file.close()
    except IOError as strerror:
        print("[gnm.py] I/O error ({0}): {0}".format(strerror))

### CODE
#ClearFile()
for user in users:    
    http = httplib2.Http()
    http.add_credentials(user, users[user]) # Basic authentication
    resp, content = http.request(gmail_feed_url , "GET", body={}, headers={} )
    dom = parseString(content)
    feed_list = dom.getElementsByTagName('entry')
    result.append(user + ": " + str(len(feed_list)))
WriteFile(result)
