import os
n=1
while(n<=10):
    os.system("fswebcam -F 4 --fps 20 -r  800*600 /home/pi/rasp/"+str(n)+".jpeg")
    print("nyc pic")
    n=n+1
exit()

