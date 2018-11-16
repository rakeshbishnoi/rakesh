#rock paper sizor
import random

#cheack for score
score_comp =0
score_player = 0


print("==================================")
print(" welcome to stone paper sizer!!!!")
print("remember 1 is stone !!")
print("remember 2 is paper !!")
print("remember 3 is sizer !!")
print("==================================")



#user input
def useinp():
    r = random.randint(1,3)
    return r
    

while True:
    r = useinp()
    x = int(input("what do u wanna throw ?"))
    if(x == 1 and r == 2):
        score_comp = score_comp + 1
        print("you lose because stone wins aginst paper!! computer scores",score_comp)
        
    elif(x == 2 and r == 1):
        score_player = score_player + 1
        print("you win because paper wins aginst stone!! your score is",score_player)
    elif(x == 1 and r == 3):
        score_player = score_player + 1
        print("you win because stone wins aginst sizer!! your score is",score_player)
    elif(x == 3 and r == 1):
        score_comp = score_comp + 1
        print("you lose because sizer wins aginst paper!! computer score is",score_comp)
    elif(x == 2 and r == 3):
        score_comp = score_comp + 1
        print("you lose because stone wins aginst paper!! computer score is",score_comp)
    elif(x == 3 and r == 2):
        score_player = score_player + 1
        print("you win because stone wins aginst paper!! your score is",score_player)
    else:
        print("u and the computer put the same values so its a draw!!")


    if(score_comp == 3):
        print("computer wins!!!")
        break
    elif(score_player==3):
        print("you win!!!")
        break
    elif(score_comp == score_player ==3 ):
        print("its a draw!!!")



