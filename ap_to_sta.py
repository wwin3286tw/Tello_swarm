#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import time


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

msg = 'command'.encode(encoding="utf-8") 
sent = sock.sendto(msg, tello_address)
time.sleep(2)

# 下一行請輸入熱點帳密，格式：ap SSID PASSWORD
msg = 'ap Android 9999999999'.encode(encoding="utf-8") 
sent = sock.sendto(msg, tello_address)
time.sleep(2)

sock.close()




