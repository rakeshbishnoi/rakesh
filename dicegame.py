import random
print("# prog to play a dice game")
while True:
	print(" press 'r' to roll the dice and 'q' to quit")
	a=input()
	if(a=='r'):
		print("you've got .... ",random.randfloat(1,2)," this time")
	if(a=='q'):
		print("bye.")
		exit()