#!/usr/bin/python

import  cgi,cgitb,os,commands,time,sys

cgitb.enable()

print   "content-type:text/html"
print   ""

recv_svc=cgi.FieldStorage()
#  recv software name from  services.html    
service=recv_svc.getvalue('service')

if  service   == 'SAAS' :
	print   "wait for  software as a service  "
	print  "<a href='http://127.0.0.1/cloudX/software.html'>"
        print   "click to get software list "
	print    "</a>"
elif  service   == 'STAAS' :
	print   "wait for storage as a service  "
	print  "<a href='http://127.0.0.1/cloudX/storage.html'>"
	print   "click to get  storage list "
	print    "</a>"
	
elif  service  ==   'PAAS' :
	print   "wait for  platform as a service  "
	print  "<a href='http://127.0.0.1/cloudX/platform.html'>"
	print   "click to get platform list "
	print   "</a>"

elif  service  ==   'IAAS' :
	print   "wait for  infrastructure as a service  "
	print  "<a href='http://127.0.0.1/cloudX/iaas.html'>"
	print   "click to get  infrastructure list "
	print    "</a>"
	
elif  service  ==   'DbAAS' :
	print   "wait for  database as a service  "
	print  "<a href='http://127.0.0.1/cloudX/database.html'>"
	print   "click to get  database list "
	print   "</a>"


