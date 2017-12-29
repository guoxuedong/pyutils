import socket
import sys
import time

def get_lock(process_name):
    global lock_socket   # Without this our lock gets garbage collected
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_socket.bind('\0' + process_name)
        print 'I got the lock'
    except socket.error:
        print 'lock exists'
        sys.exit()


get_lock('running_test')
while True:
    time.sleep(3)
