#!/usr/bin/python
# -*- coding: utf-8 -*-
from serial import Serial
import sys
import time
import codecs
import datetime
from datetime import datetime
from time import sleep
import mymodule
import string
import logging


logtime = str(datetime.now().strftime('%Y%m%d'))
lgr = logging.getLogger('Onstartup')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
fh = logging.FileHandler('/home/pi/projects/scripts/log/onstartup.log')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)


f = open("/etc/hostname","r") #opens file with name of "test.txt"
myhostname = f.read().replace('\n', '')
mytime = str(datetime.now().strftime('%H:%M:%S'))
myip=mymodule.myip()
try:
	mymodule.r.hmset(myhostname, {'ip':myip,'external_ip':mymodule.publicip()})
except:
	print "unable redis"
try:
	mymodule.mysendmail('roni.segoly@gmail.com',myip,myhostname + " just started")
except:
	print "unable email" 
lgr.info(myip)
