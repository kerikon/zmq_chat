import zmq
import time
import sys
from threading import Thread

def room(port):
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://10.0.0.4:" + port)

	while(True):
		#  Wait for next request from client
    		message = socket.recv()
    		print("\n%s" % message)
		print('<You>: ')

    		#  Do some 'work'
    		time.sleep(1)

    		#  Send reply back to client
    		socket.send("")

if len(sys.argv) == 4:
	
	t = Thread(target=room, args=(sys.argv[2],))
	t.start()

	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://10.0.0.4:" + sys.argv[3])

	name = sys.argv[1]

	while True:
		input = raw_input('<You>: ')

		socket.send("<" + name + ">: " + input)

		msg = socket.recv()

else:
	print "Need 3 parameters"
