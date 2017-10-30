import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.0.0.14:5555")

while True:
	input = raw_input('Write Message: ')

	socket.send(input)

	msg = socket.recv()
