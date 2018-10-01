#prog to build snake n ladder game using dictionary
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
		snake={11:2,25:4,38:9,65:46,89:70,93:64}
		ladder={13:34,8:37,40:68,52:81,76:97}
		if(count==snake):
			print("oops!! you steped on a snake")
			print("now, your position is,",count)
		elif(count==ladder):
			print("yeah!! you've got a ladder!!!")
			print("now, your position is,",count)
		elif(count==100):
			print("congradulations!!! you have won the game!!!")
			count=count-p
		elif(count>100)
			print("you can't go beyond 100.")
			count=count-p
			print(" now, your position is,",count)
	if(a=='q'):
			print("bye. hope we'd play another time...  :(")
			exit()