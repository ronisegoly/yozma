#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/bbt
python /home/pi/projects/scripts/onstartup.py
python /home/pi/projects/scripts/sensor_to_txt.py 
#  >/var/log/sensor.log 2>&1
cd /
