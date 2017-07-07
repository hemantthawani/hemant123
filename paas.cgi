#!/usr/bin/python
import cgi,os,commands,cgitb
cgitb.enable()
 

print "content-type:text/html"
print ""
data=cgi.FieldStorage()
x=data.getvalue('paas')


if x  ==  'py'  :
     print "code in python"


