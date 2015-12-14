ports = ['/dev/ttyACM0','/dev/ttyUSB0','/dev/ttyUSB1','NULL']

from serial import Serial
import time
import datetime
import sys
from datetime import datetime
from time import sleep
import mymodule
import string
import phant
import mymodule
import urllib
import urllib2
import logging
import pdb
import serial
import json


logtime = str(datetime.now().strftime('%Y%m%d'))
logging_date=logtime

mydate= str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
#pdb.set_trace()
lgr = logging.getLogger('Sensor')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
fh = logging.FileHandler('/home/pi/projects/scripts/log/%ssensor.csv'%logtime)
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)


f = open("/etc/hostname","r") #opens file with name of "test.txt"
myhostname = f.read().replace('\n', '')

for p in ports:
        try:
                print "trying port: "+p
                if (p=='NULL'):
                        print "getting off"
                        sys.exit()
                ser = Serial(p, 9600)
                break
        except:
                print "error connecting...aborting" + p
                #sys.exit()
time.sleep(4)


while True:
     #get new command from redis
#     command="none"
      #check if it's new day, if yes create new file
     logtime = str(datetime.now().strftime('%Y%m%d'))
     if (logging_date<>logtime):#time for mew log file
            logging_daye=logtime
            lgr.removeHandler(fh)
            fh = logging.FileHandler('/home/pi/projects/scripts/log/%ssensor.csv'%logtime)
            fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
            frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
            fh.setFormatter(frmt)
            lgr.addHandler(fh)
     try:
        command = mymodule.r.hmget(myhostname,'command')[0]
	print "received command :"+command
#        mymodule.r.hmset('aqua001',{'command':'none'})
        ser.write(command) # Convert the decimal number to ASCII then send it to the Arduino
	time.sleep(1)
     except Exception as s:
        print s.message	
     line = ser.readline() # Read the newest output from the Arduino
     print line
     try:
	j=json.loads(line)
#	pdb.set_trace()
    	print "ec",j
#addding the date
	mydate= str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
	j[u'mydate']=unicode(mydate)

	print j
	try:
#creating message for log as csv
        	with open("/home/pi/projects/scripts/sensor.txt", "w") as text_file:
			message = ""
			for key in j:
			        print j[key]
			        message= message + str(j[key])
			        message = message + ","
			#        print message
		        m=message[:-1]
		        print m
                	lgr.info(m)#"%.2f,%.2f,%.2f,%s"%(j["A0"],j['A1'],j["A2"],"0,0,0,0,0"))
                        print "logeed line added"
			print j
			#pdb.set_trace()
                        text_file.write(json.dumps(j))
                text_file.close()
        except Exception as s:
                print s.message
     except Exception as s:
	print s.message
     sleep(6)


