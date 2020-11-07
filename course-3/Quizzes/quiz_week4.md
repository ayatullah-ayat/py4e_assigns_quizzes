** 1. Which of the following Python data structures is most similar to the value returned in this line of Python:
	``x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')``
1]	regular expression
2]	dictionary
3]	file handle
4]	socket
5]	list
Answer: 3]

	** 1. Question 2 In this Python code, which line actually reads the data?
		`` import socket``

		``mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mysock.connect(('data.pr4e.org', 80))
		cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
		mysock.send(cmd)``

		``while True:
		    data = mysock.recv(512)
		    if (len(data) < 1):
		        break
		    print(data.decode())
		mysock.close() ``

``


1]	mysock.recv()
2]	socket.socket()
3]	mysock.close()
4]	mysock.connect()
5]	mysock.send()
Answer:	1]