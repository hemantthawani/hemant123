#!/usr/bin/python
import os,commands,cgi,time,sys,cgitb
cgitb.enable()
print   "content-type:text/html"
s=cgi.FieldStorage()

os=s.getvalue('os_name')
ram=s.getvalue('os_ram')
core=s.getvalue('os_cpu')
hdd=s.getvalue('os_hdd')
port=s.getvalue('port')

install_os="sudo virt-install --name "+os+"  --ram "+ram+" --vcpu"+core+"  --nodisk --cdrom /root/Downloads/kali.iso  --graphics  vnc,listen=127.0.0.1,port="+port
print install_os

