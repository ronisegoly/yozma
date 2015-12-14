import time
import datetime
import sys
from datetime import datetime
from time import sleep
import mymodule
import string
#import phant
import urllib
import urllib2
import pdb
import json
#pdb.set_trace()

f = open("/etc/hostname","r") #opens file with name of "test.txt"
myhostname = f.read().replace('\n', '')


mytime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
shorttime=str(datetime.now().strftime('%H%M%S'))
try:
	with open("/home/pi/projects/scripts/sensor.txt", "r") as text_file:
        	x= text_file.read().strip()
      		text_file.close()
except Excpetion, s:
	print 'unable to open file' + str(s)
print "x",x
try:
	j = json.loads(x)
	print "j"
	try:
		mymodule.r.hmset(myhostname, {'time':mytime})
#		pdb.set_trace()
		for key in j:
			if key<>"command":
				print "setting",key,j[key]
				mymodule.r.hmset(myhostname,{key:j[key]})
		print 'redis demo set'
	except Exception, s:
		print "error using redis" + str(s)
except Exception as s:
	print s.message



