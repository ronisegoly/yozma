import signal
import smtplib
import os
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

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)


def mysendmail(to,message,subject):
        user =mymodule.parser.get('Mail','user')
        password =mymodule.parser.get('Mail','password')
        # The actual mail send
#        pdb.set_trace()
	server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(user,password)
        msg = 'Subject: %s\n\n%s' % (subject, message)
        server.sendmail(user,to, msg)
        server.quit()

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
#print "x",x
#pdb.set_trace()
j=json.loads(x)
value = j['mydate']
print value
d1 = datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
d2=datetime.now()
delta = (d2-d1).total_seconds()/60
print "delta in time",delta
#it's time to act
if (delta>25):	
	try:
		mysendmail(mymodule.parser.get('Mail','sendto'),"Sensor process is down for %s minutes "% (delta),myhostname +" reports process is late")
	except Exception as s:
		print s.message
	print "mail sent"
	check_kill_process("sensor_to_txt.py")
	print "instance killed"
	os.system("python /home/pi/projects/scripts/sensor_to_txt.py &")
	print "instance restarted"

