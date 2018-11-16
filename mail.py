#/usr/bin/python3
import smtplib
import getpass

myemail=input("enter your email in double quotes")
password=getpass.getpass()
sendermail=input("enter the sender mail id in double quotes")
s = smtplib.SMTP('smtp.gmail.com',587)

#TLS
s.starttls()

s.login(myemail,password)

message = "hello"

s.sendmail(sendermail,myemail,message)


s.quit

