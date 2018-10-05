import random
while(1):
	print(tq u to play game)
		d={1:'R',2:'P',3:'S'}
		a=d[random.randint(1,3)]
		u=int(input("enter 'R','P','S' "))
		if(c=='R' and u=='S') or (c=='P' and u=='R') or (c=='S' and u=='P'):
			print("computer win")
		elif(c=='R' and u=='P') or (c=='P' and u=='S') or (c=='S' and u=='R'):
			print("user win")
		elif(c==u):
			print("tie")
