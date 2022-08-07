#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
from URL_Lookup_Service.URL_Lookup_Service import URL_Lookup_Service
import json

CGI = True
MalwareURL = True


cgitb.enable()
print "Content-Type: text/plain;charset=utf-8"
print
form = cgi.FieldStorage()

if CGI:
    URL = form["Field"].value
else:
    URL = "bolo100.com"

LookupInst = URL_Lookup_Service(URL)

try:
    MalwareURL = LookupInst.lookup()
except:
    print "lookup Error"
    raise

response = {}
if MalwareURL:
    response[URL] = "Malware"
    # print "URL is Malware (Not Safe)"
else:
    response[URL] = "Safe"
    # print "URL is Safe"
print json.dumps(response)
