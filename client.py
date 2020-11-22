import socket 

HOST = 'localhost'
PORT = 6969
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    data = s.recv(1024)
    data = data.decode()
    print('Server:',data)
    message = str(input('You:'))
    message = message.encode()
    s.send(message)
    