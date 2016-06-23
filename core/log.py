import datetime
import io

time = datetime.datetime.now()
logfilename = str(time)
logfile = open('core/log/'+logfilename+'.log', 'a')

def printlog(*log):
	global time
	global logfile
	line = str(time)+' '+str(log[0])+'\n\n'
	logfile.write(line)
	print(time,str(log[0])+'\n')

def log(*log):
	global time
	global logfile
	line = str(time)+' '+str(log[0])+'\n\n'
	logfile.write(line)