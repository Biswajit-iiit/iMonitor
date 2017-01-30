import os
import time
import pyttsx

engine = pyttsx.init()
path = '/home/biswajit/work/monitor/output.txt'
        # /home/biswajit/work/monitor/output.txt
cmd = 'top -n1 -b>{}'.format(path)
print cmd
os.environ['TERM'] = 'xterm'
while(1<2):
	print os.system(cmd)
	break

log = open(path,'r')
# print len(log.readlines())

log_arr = log.readlines()
log.close()

print len(log_arr)
print len(log_arr)
print list(set(log_arr[7].split(' '))).remove('')
x = log_arr[7].split()
y = log_arr[8].split()
z = log_arr[9].split()

MAX_CPU_USAGE = 80
MAX_MEM_USAGE = 60

if x[-3] >= MAX_MEM_USAGE:
	msg = "Heavy memory usage by {}".format(x[-1])
	# engine.say(msg)
	# engine.runAndWait()
	os.system("espeak {}".format(msg))
	time.sleep(5)
if x[-4] >= MAX_CPU_USAGE:
	msg = "Heavy cpu usage by {}".format(x[-1])
	# engine.say(msg)
	# engine.runAndWait()
	os.system("espeak {}".format(msg))
	time.sleep(5)

if y[-3] >= MAX_MEM_USAGE:
	msg = "Heavy memory usage by {}".format(y[-1])
	# engine.say(msg)
	# engine.runAndWait()
	os.system("espeak {}".format(msg))
	time.sleep(5)
if y[-4] >= MAX_CPU_USAGE:
	msg = "Heavy cpu usage by {}".format(y[-1])
	# engine.say(msg)
	# engine.runAndWait()
	os.system("espeak {}".format(msg))
	time.sleep(5)

if z[-3] >= MAX_MEM_USAGE:
	msg = "Heavy memory usage by {}".format(z[-1])
	# engine.say(msg)
	# engine.runAndWait()
	os.system("espeak {}".format(msg))
	time.sleep(5)
if z[-4] >= MAX_CPU_USAGE:
	msg = "Heavy cpu usage by {}".format(z[-1])
	# engine.say(msg)
	os.system("espeak {}".format(msg))
	time.sleep(5)
	# engine.runAndWait()
