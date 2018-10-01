import random
print(" welcome to the snake and ladder game!!!!!")
print(" you can start playing th egame only if you get 1 or 6")
while True:
	print(" press 'r' to roll the dice and press 'q' to quit the game ")
	a=input()

	def dice():
		d=(random.randint(1,6))
		return(d)

	if(a=='q'):
		print("bye... i hope you'll come back again to play..  :(")
		exit()

	if(a=='r'):
		p=dice()
		print(" you have got",p)
		if(p==1):
			print(" congradulations you have entered the game!! and your position is 1")
		elif(p==6):
			print(" congradulations you have entered the game!! and your position is 1")
		else:
			print(" awwww.... try again")
		
	