#!/usr/bin/python
# Filename: mymodule.py
def send_attachment(sendto,filename,subject,message):
	emailfrom =parser.get('Mail','user')
	emailto = sendto
	fileToSend = filename
	user = parser.get('Mail','user')
	password = parser.get('Mail','password')
	msg = MIMEMultipart()
	msg["From"] = emailfrom
	msg["To"] = emailto
	msg["Subject"] = subject
	msg.preamble = message

	ctype, encoding = mimetypes.guess_type(fileToSend)
	if ctype is None or encoding is not None:
    		ctype = "application/octet-stream"

	maintype, subtype = ctype.split("/", 1)
	if maintype == "text":
	    fp = open(fileToSend)
	    # Note: we should handle calculating the charset
	    attachment = MIMEText(fp.read(), _subtype=subtype)
	    fp.close()
	elif maintype == "image":
	    fp = open(fileToSend, "rb")
	    attachment = MIMEImage(fp.read(), _subtype=subtype)
	    fp.close()
	elif maintype == "audio":
	    fp = open(fileToSend, "rb")
	    attachment = MIMEAudio(fp.read(), _subtype=subtype)
	    fp.close()
	else:
	    fp = open(fileToSend, "rb")
	    attachment = MIMEBase(maintype, subtype)
	    attachment.set_payload(fp.read())
	    fp.close()
	    encoders.encode_base64(attachment)
	attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
	msg.attach(attachment)

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(user,password)
	server.sendmail(emailfrom, emailto, msg.as_string())
	server.quit()



def hostbyname(hostname):
	return socket.gethostbyname(hostname)
def myip():

	try:
		return(commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:])
	except:
		return "unkown"

def publicip():
	try:
		ipreq=urllib2.Request("http://wtfismyip.com/text")
	       	ipres=urllib2.urlopen(ipreq)
	        ipdata = ipres.read()
	        return(ipdata)
	except:
        	return("unknown")


def mysendmail(to,message,subject):
	username = parser.get('Mail','user')
	password = parser.get('Mail','password')
	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	msg = 'Subject: %s\n\n%s' % (subject, message)
	server.sendmail(username,to, msg)
	server.quit()
	
from urllib import pathname2url
import urllib2
from datetime import datetime
import smtplib
import ast
import argparse
from ConfigParser import SafeConfigParser
import socket
import gmail
import json
import sys
import urllib
import commands

#import mylcd
import ftplib
import json
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


parser = SafeConfigParser()
parser.read('/home/pi/projects/scripts/mymodule.cfg')
import redis
r = redis.StrictRedis(host='23.251.149.210', port=6379, db=0, password='yozma1234')

# End of mymodule.py
import logging
syslog = logging.getLogger('Syslog')
syslog.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
fh = logging.FileHandler('/home/pi/projects/scripts/log/syslog')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
syslog.addHandler(fh)


