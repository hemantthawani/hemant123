#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "content-type:text/html"
print   ""

data=cgi.FieldStorage()
#  recv software name from  os_service.html    
software=data.getvalue('os_service')

if  software   ==   'live' :
	print   "wait for  os to be live  "
	print  "<a href='http://127.0.0.1/cgi-bin/'>"
	print   "click to get  firefox "   
	print   "</a>"

elif  software  ==   'install' :
	print   "wait for  install  "
        print  "<a href='http://127.0.0.1/cgi-bin/gedit.cgi'>"
	print   "click to get text editor "
	print   "</a>"

elif  software  ==   'installed' :
	print   "wait for  installed version  "
        print  "<a href='http://127.0.0.1/cgi-bin/vlc.cgi'>"
	print   "click to get  firefox "   
	print   "</a>"

