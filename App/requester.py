
import sys
import os
import re
import lxml
from lxml import html
import Objects.zetypes as zetypes
import io
from urllib.parse import urlparse


def getFields(headers):
	fields={}
	i=1
	for header in headers:
		if len(header)==0:
			continue
		if header.find(" ")==0 or header.find("\t")==0:
			continue
		if len(header.split(":"))>=2:
			key = header.split(":")[0].strip()
			if key in fields:
				#fields[key]=fields[key]+" "+header[header.find(":")+1:].strip()
				continue
			else:
				fields[key]=header[header.find(":")+1:].strip()
		# end of the else
		else:
			# else for [if len(header.split(":"))>=2: ]
			#print("ERROR: RFC VIOLATION 3") DON't worry
			dontworry = 1
	return fields



# разбор заголовков запроса
def getHeaders(content):
	req = zetypes.ZeRequest()
	fields={}

	headerSection=content.split("\r\n\r\n")[0]
	headerLines=headerSection.split("\r\n")
	firstLine=headerLines[0]

	allFields=firstLine.split("\\r\\n")
	firstLineFields=firstLine.split(" ")

	if len(allFields)>1:
		fields=getFields(allFields[1:])
	if len(firstLineFields)>=3:                     
		if firstLine.find("HTTP")==0:
			fields["Version"]=firstLineFields[0]
			fields["Status-code"]=firstLineFields[1]
			fields["Status-desc"]=" ".join(firstLineFields[2:])
		else:
			fields["Method"]=firstLineFields[0]
			fields["URL"]=firstLineFields[1]
			fields["Version"]=firstLineFields[2]
	else:
		print("ERROR: RFC VIOLATION 2")
	req.setHeaders(fields)
	return req





# разбор параметров из GET запроса
def parseParams(requester):
	url = requester.getHead("URL")
	# https://docs.python.org/3/library/urllib.parse.html
	o = urlparse(url);
	#o = urlparse.parse_qs(url.encode('ASCII'))
	requester.setPath(o.path)

	params = {}
	sp = o.query.split("&")
	for s in sp:
		dd = s.split("=")
		if len(dd) >= 2:
			params[dd[0]] = dd[1]

	requester.setParams(params)
	return 0;
