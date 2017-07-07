#!/usr/bin/python

import os,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

iaas_ip="127.0.0.12"
iaas_port=5555

os_name=raw_input("enter os name : ")
os_ram=raw_input("enter os ram in MB : ")
os_cpu=raw_input("enter os cpu in CORE : ")
os_hdd=raw_input("enter os hard disk in GB : ")

s.sendto(os_name,(iaas_ip,iaas_port))
s.sendto(os_ram,(iaas_ip,iaas_port))
s.sendto(os_cpu,(iaas_ip,iaas_port))
s.sendto(os_hdd,(iaas_ip,iaas_port))
