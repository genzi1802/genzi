import socket


HOST = 'localhost'
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)
conn, addr = s.accept()


print('Connect by',addr)
while True:
    message = str(input('You:'))
    message = message.encode()
    conn.send(message)
    data = conn.recv(1024)
    data = data.decode()
    print('Client:',data)
            
            
