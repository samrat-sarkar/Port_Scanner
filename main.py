import os
import sys
import socket
import ipaddress
from urllib.parse import urlparse
import csv

def main():
    print("""\033[1;32m
  _____           _      _____                                 
 |  __ \         | |    / ____|                                
 | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|                                                                 
    """)
    print("""\033[1;32m
 +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+
 | By  s a m r a t   S a r k a r |
 +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+
    """)
    def check(host, port, sn):
        timeout_seconds = 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_seconds)
        result = sock.connect_ex((host, int(port)))
        if result == 0:
            print("\033[1;32m Port: {} is OPENED || Service : {}".format(port, sn))
        else:
            print("\033[1;31m Port: {} is CLOSED".format(port))
        sock.close()

    def scan(host):
        with open('ports.csv') as file_obj:
            heading = next(file_obj)
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                port = row[1]
                sn = row[0]
                check(host, port, sn)
            print("\033[1;32m Task Completed")

    try:
        t = sys.argv[1]
        v = sys.argv[2]
    except:
        print("\033[1;31m Incomplete Arguments !")
    if t == "url":
        temp = v
        parts = urlparse(temp)
        temp = parts.hostname
        if temp != None:
            url = temp
        try:
            host = socket.gethostbyname(url)
            scan(host)
        except Exception as e:
            if 'getaddrinfo failed' in str(e):
                print("\033[1;31m Enter Valid URL ( Eg: https://www.example.com/ )")
    elif t == "ip":
        try:
            ipaddress.ip_address(v)
            scan(v)
        except Exception as e:
            if 'does not appear to be an IPv4 or IPv6 address' in str(e):
                print("\033[1;31m Enter Valid IP ( Eg: 192.168.1.1 )")
    else:
        print("\033[1;31m Incorrect Arguments ! ")
        print("\33[1;93m Eg: python main.py url https://www.example.com/")
        print("\33[1;93m --------------------OR-------------------------")
        print("\33[1;93m Eg: python main.py ip 192.168.1.1 ")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\033[1;31m *******************PROGRAM-ENDED*******************')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)