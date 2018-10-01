# prog to play snake and ladder game
import random
print("     welcome to the snake and ladder game!!!   ")
def dice():
	d=(random.randint(1,6))
	return d
count=0	
while(count<=100):
	print("press 'r' to roll the dice or press 'q' to quit the game")
	a=input()
	if(a=='r'):
		p=dice()
		print(" you have got...",p)
		count=count+p
		print(" and  your position is,",count)
		if(count==11):
			count=2
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==25):
			count=4
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==38):
			count=9
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==65):
			count=46
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==89):
			count=70
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==93):
			count=64
			print("oops!! there was a snake over there!!..")
			print(" now, your position is,",count)
		elif(count==13):
			count=34
			print("yeah!! you've got the ladder!!..")
			print(" now, your position is,",count)
		elif(count==8):
			count=37
			print("yeah!! you've got the ladder!!..")
			print(" now, your position is,",count)				
		elif(count==40):
			count=68
			print("yeah!! you've got the ladder!!..")
			print(" now, your position is,",count)
		elif(count==52):
			count=81
			print("yeah!! you've got the ladder!!..")
			print(" now, your position is,",count)
		elif(count==76):
			count=97
			print("yeah!! you've got the ladder!!..")
			print(" now, your position is,",count)
		elif(count==100):
			print("    congradulations!!! you won the game")
			count=count-p
		elif(count>100):
			print("you can't go beyond 100.")
			count=count-p
			print(" now, your position is,",count)
	if(a=='q'):
			print("bye. hope we'd play another time...  :(")
			exit()
