import subprocess
from subprocess import PIPE, STDOUT
from time import sleep
from datetime import datetime

vd = "0" #video device
fn="rsa_key_captured.jpeg"
cmd="v4l2-ctl -d"+vd+" -c focus_auto=0"
p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()
print output, err

def capture_image():
	cmd="v4l2-ctl -d"+vd+" -c focus_absolute=120; v4l2-ctl -d"+vd+" -l"
	p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	print output, err

	cmd="v4l2-ctl -d"+vd+" -c focus_absolute=100; v4l2-ctl -d"+vd+" -l"
	p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	print output, err

	cmd="ffmpeg -f video4linux2 -i /dev/video"+vd+" -vframes 1 " + fn
	p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	print output, err

while(True):
	capture_image()
	f = open('/var/www/html/rsa_key_timestamp.txt', 'w')
	print(datetime.now())

	f.write(str(datetime.now()))
	f.close()


	sleep(10)
	print "!captured"
