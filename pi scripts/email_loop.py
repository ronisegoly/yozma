dict={'takeone':'takeone()','shutdown':'poweroff()','email':'get_email()','level':'level(email)','help':'help()'}
#                        os.system(dict[command])

def takeone():
#	print sent_from
	f = open("/etc/hostname","r") #opens file with name of "test.txt"
	mytime = str(datetime.now().strftime('%Y%m%d%H%M%S'))
	fn = "/tmp/"+mytime+".jpg"
	try:
        	msg= "fswebcam --title %s -S 50 -r 640X480 --jpeg 95" %(fn)
        	os.system(msg+" "+fn)
	except:
        	print "unable to take picture"
	try:
        	print "sending file " + fn
        	mymodule.send_attachment(sent_from,fn,"The picture you just took", "enjoy")
	except:
        	print "unable to send"
#       sleep(3600)
def poweroff():
	os.system("sudo shutdown now -h")
def get_email():
	msg=mymodule.myip()
	f = open("/etc/hostname","r") #opens file with name of "test.txt"
	myhostname = f.read().replace('\n', '')
        mysendmail(email.fr,msg,"Sensors data from Aquaphonic system "+myhostname)

def help():
        msg="Availabale commands (please include in subject)\nhelp\nlevel\nshutdown\ntakeone"
        mysendmail(email.fr,msg,"Sensors data from Aquaphonic system aqua001")

def level(email):
	r = redis.StrictRedis(host='23.251.149.210', port=6379, db=0, password='yozma1234')	
	try:
#        pdb.set_trace()
        	v1,v2,v3,v4,v5=r.hmget('aqua001','V1','V2','V3','V4','V5')
        	mytime = str(datetime.now().strftime('%D %H:%M:%S'))
        	msg="Date&Time-%s\nPH-%s\nEC-%s\nWtemp-%s\nTemp-%s\nHumidity-%s"%(mytime,v1,v2,v3,v4,v5)
	except:
        	v1=v2=v3=v4=v5=0

	msg=mymodule.myip()
        f = open("/etc/hostname","r") #opens file with name of "test.txt"
        myhostname = f.read().replace('\n', '')
	mysendmail(email.fr,msg,"Sensors data from Aquaphonic system "+ myhostname)

def mysendmail(to,message,subject):
	user =mymodule.parser.get('Mail','user')
	password =mymodule.parser.get('Mail','password')
        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(user,password)
        msg = 'Subject: %s\n\n%s' % (subject, message)
        server.sendmail(user,to, msg)
        server.quit()

import mymodule
import smtplib
#import mydb
import gmail 
from datetime import datetime
#import OpenSSL
#import json
import os
import redis
import pdb
import logging
#pdb.set_trace()
logtime = str(datetime.now().strftime('%Y%m%d'))
logging_date=logtime
lgr = logging.getLogger('Sensor')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
fh = logging.FileHandler('/home/pi/projects/scripts/log/%semail.log'%logtime)
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)
user =mymodule.parser.get('Mail','user')
password =mymodule.parser.get('Mail','password')


r = redis.StrictRedis(host='23.251.149.210', port=6379, db=0, password='yozma1234')
g = gmail.login(user,password)
unread = g.inbox().mail(unread=True)
for email in unread:
	email.fetch()
	print "Email sent to %s" %email.fr
	try:
		sent_from=email.fr
		mytime=str(datetime.now().strftime('%H:%M'))

                lgr.info(mytime+" exceuting "+dict[email.subject])

		exec(dict[email.subject])
	except:
		help()
#	level(email)
	#	print email.subject
	#print email.sender
	email.read()
