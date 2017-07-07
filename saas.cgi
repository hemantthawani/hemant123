#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "content-type:text/html"
print   ""

data=cgi.FieldStorage()
#  recv software name from  services.html    
software=data.getvalue('soft')

if  software   ==   'firefox' :
	print   "wait for  firefox  "
	print  "<a href='http://127.0.0.1/cloudX/firefox.sh'>"
	print   "click to get  firefox "   
	print   "</a>"

elif  software  ==   'gedit' :
	print   "wait for  text editor  "
        print  "<a href='http://127.0.0.1/cloudX/gedit.sh'>"
	print   "click to get text editor "
	print   "</a>"

elif  software  ==   'vlc' :
	print   "wait for  media player  "
        print  "<a href='http://127.0.0.1/cloudX/vlc.sh'>"
	print   "click to get  firefox "   
	print   "</a>"

elif  software  ==   'calc' :
	print   "wait for  calcccc "
        print  "<a href='http://127.0.0.1/cloudX/calc.sh'>"
	print   "click to get  calc "   
	print   "</a>"


