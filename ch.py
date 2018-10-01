import random
print("     welcome to the snake and ladder game!!!   ")
def dice():
	d=(random.randint(1,6))
	return d
count=0	
while(count<=100):
	a=input("press 'r' to roll the dice or press 'q' to quit the game")
	if(a=='r'):
		p=dice()
		print(" you have got...",p)
		count=count+p
		print(" and  your position is,",count)