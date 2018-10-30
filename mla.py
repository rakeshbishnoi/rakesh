import smtplib
import getpass

myemail=input("your email id:")
password=getpass.getpass()
racemail=input("receiver's email id:")

# creates SMTP session
s=smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(myemail, password)

# message to be sent
message="hi "

# sending the mail
s.sendmail(myemail, racemail, message)

# terminating the session
s.quit()