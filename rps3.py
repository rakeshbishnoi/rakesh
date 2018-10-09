import random
a={1:'r',2:'p',3:'s'}
c=a[random.randint(1,3)]
u=int(input("enter 'R','P','S' "))
if(c=='R' and u=='S') or (c=='P' and u=='R') or (c=='S' and u=='P'):
	print("computer win")
elif(c=='R' and u=='P') or (c=='P' and u=='S') or (c=='S' and u=='R'):
	print("user win")
elif(c==u):
	print("tie")
else:
	print("you won")