files=[['keep_alive.sh','/home/pi/projects/scripts'],['sensor_to_txt.py','/home/pi/projects/scripts'],
['email_loop.py','/home/pi/projects/scripts'],['mymodule.py','/home/pi/projects/scripts'],
['mymodule.cfg','/home/pi/projects/scripts'],['from_dropbox.py','/home/pi/projects/scripts'],
['sensor_to_redis.py','/home/pi/projects/scripts'],['ftp_clean_file.py','/home/pi/projects/scripts']]
location=[]
from subprocess import call  
print "listing"
file = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh list"
print file
call ([file], shell=True)

for line in files:
	file = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh download %s %s" %(line[0],line[1])
	print file 
	call ([file], shell=True)

