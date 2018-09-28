import random 
count=0
while(count<=100):
	a=input("enter 1 to roll and 0 to quite:")
	if(a==1):
		a=random.randint(1,6)
		count=count+a
		print("ur position",random.randint(1,6),count)

		if(count==8):
			count=37
			print("cong!!! u got ladder")
		elif(count==11):
			count=2
			print("sorry!!! snake ate u")
		elif(count==13):
			count=34
			print("cong!!! u got ladder")
		elif(count==25):
			count=4
			print("sorry!!! snake ate u")
		elif(count==38):
			count=9
			print("sorry!!! snake ate u")
		elif(count==40):
			count=68
			print("cong!!! u got ladder")
		elif(count==52):
			count=81
			print("cong!!! u got ladder")
		elif(count==65):
			count=46
			print("sorry!!! snake ate u")
		elif(count==76):
			count=97
			print("cong!!! u got ladder")
		elif(count==89):
			count=70
			print("sorry!!! snake ate u")
		elif(count==93):
			count=64
			print("sorry!!! snake ate u")
		elif(count>100):
			print("u nan't go beyond 100")
			count=count-a
		elif(count==100):
			print("congrats,u won")