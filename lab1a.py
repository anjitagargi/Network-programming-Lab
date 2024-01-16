
import socket

host = 'local host'
port = 7000

s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM)

s.bind(('', port))

#maximum commands it can take
s.listen(1)  
c, addr = s.accept()

print("CONNECTION FROM:", str(addr))
c.send(b"HELLO WORLD, \
	THIS IS NETWORK PROGRAMING LAB1 EXECUTION")

msg = "STAY TUNED FOR NEXT LAB"
c.send(msg.encode())

# disconnect the server
c.close()
