import socket
import threading
import time
from stats import Stats

class Tello:
    def __init__(self, ip_list):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        #self.tello_ip = '192.168.10.1'
        #self.tello_ip_list = ['192.168.43.4','192.168.43.40']
        self.tello_ip_list = ip_list
        self.qty = len(ip_list)
        self.log = []
        self.MAX_TIME_OUT = 6

        #self.tello_port = 8889
        #self.tello_adderss = (self.tello_ip, self.tello_port)
        #self.log = []

    def send_command(self, command):

        for ip in self.tello_ip_list:
            _ip = ip.rstrip()

            # skip line begining with '#''
            if '#' in _ip:
                continue

            self.socket.sendto(command.encode('utf-8'), (_ip, 8889))
            
            # add command to log    
            print(_ip + ' ' + command)   
            self.log.append(Stats(command, len(self.log)))
            

            ''' wait till command finished
            start = time.time()         
            while not self.log[-1].got_response():
                now = time.time()
                diff = now - start
                if diff > self.MAX_TIME_OUT:
                    print('time out')
                    return
            print(_ip + ' ' + command + ' done')
            '''
                

    def _receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('%s: %s' % (ip, self.response))
                self.log[-1].add_response(self.response)
            except socket.error:
                print ("Caught exception socket.error : %s" )

    def on_close(self):
        #pass
        #for ip in self.tello_ip_list:
        #    self.socket.sendto('land'.encode('utf-8'), (ip, 8889))
        self.socket.close()

    def get_log(self):
        return self.log

