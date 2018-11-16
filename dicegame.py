import random


i = 0
while True:
    x = input("press r to roll and q to quit")
    if(x=="r"):
        print(random.randint(1,6))
    elif(x=="q"):
        print("sorry u lose")
        exit()
    else:
        print("Enter a valied alphabet")
        
