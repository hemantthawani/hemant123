#!/usr/bin/python


import cgi,os,time,sys,cgitb
cgitb.enable()

print  "content-type:text/html"
print ""

#this id for rec data from cloud
recv=cgi.FieldStorage()
user=recv.getvalue('u')
password=recv.getvalue('p')


print  user
print  password


if   user == 'root' and password == 'redhat1' :


 	print "login done"
  

else  :
  
        print "you went something wrong"
       
   	
