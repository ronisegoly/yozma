import os
import sys
import pdb
import datetime
import sys
from datetime import datetime
import subprocess

path = '/home/pi/projects/scripts/log/'
logtime = str(datetime.now().strftime('%Y%m%d'))
print logtime
for file in os.listdir(path):
        if (file.find("csv")>-1):
                if (file.find(logtime)>-1):
                        print "todays log, not touching " +file
                else:
                        print "Will be uploaded and deleted " + file
#                       pdb.set_trace()
			msg = "~/Dropbox-Uploader/dropbox_uploader.sh upload %s%s /log/ " %(path,file)
			print msg
			#os.system(msg)
			#we will delte the file only of uplaoded
			proc = subprocess.Popen([msg, ''], stdout=subprocess.PIPE, shell=True) 
			(out, err) = proc.communicate()
			if (out.find('DONE')<0):
				print 'error'  
			else:	
				os.remove(path+file)
