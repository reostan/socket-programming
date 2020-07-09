#for server module
import socket
s = socket.socket()
print("The socket has been created")
s.bind(("localhost", 9999))
s.listen(3)
print("waiting for the connections")
while True:
    c, address = s.accept()
    print(" The info received")
    name = c.recv(1024).decode()
    print("Connected with", address, name)


    c1, address = s.accept()
    print(" The info received")
    name = c1.recv(1024).decode()
    print("Connected with", address, name)


    text1 = c.recv(1024).decode()
    text = c1.recv(1024).decode()

    c.send(bytes(text, 'utf-8'))
    c1.send(bytes(text1, "utf-8"))
    
 #for clientmodule
 import socket
c = socket.socket()
c.connect(("localhost", 9999))
name = input("enter your name")
c.send(bytes(name, "utf-8"))

while True:
    text1 = input("info for Nishan")
    c.send(bytes(text1, 'utf-8'))
    print(c.recv(1024).decode())
  
 #for client1 module
 import socket
c1 = socket.socket()
c1.connect(("localhost", 9999))
name = input("enter your name")
c1.send(bytes(name, 'utf-8'))

while True:
    text = input("info for Saraj")
    c1.send(bytes(text, 'utf-8'))
    print(c1.recv(1024).decode())
