#http://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/
#this script runs by crontab every XX , if no internet conenct it will reboot
#Should be executeable sudo chmod 775 /usr/local/bin/keep_alive.sh
ping -c4 google.com > /dev/null
if [ $? != 0 ]
then
  sudo /sbin/shutdown -r now
fi
