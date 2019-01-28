# tello_test.py ip.txt cmd.txt

from tello import Tello
import sys
from datetime import datetime
import time


if len(sys.argv) != 3:
    print("Please run : python main.py ip.txt cmd.txt")
    sys.exit(0)

#start_time = str(datetime.now())

#read command file
file_name1 = sys.argv[1]
f_ip = open(file_name1, "r")
ip_list = f_ip.readlines()

file_name2 = sys.argv[2]
f_cmd = open(file_name2, "r")
commands = f_cmd.readlines()

tello = Tello(ip_list)
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            #print 'delay %s' % sec
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

''' logging
log = tello.get_log()
out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
'''