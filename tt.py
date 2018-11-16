
import random

a = ["1","2","3","4","5","6","7","8","9"]


def print_board():
    print("       |             |       ")
    print("       |             |       ")
    print("    ",a[0],"| ","    ",a[1],"    | ",a[2])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",a[3],"| ","    ",a[4],"    | ",a[5])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",a[6],"| ","    ",a[7],"    | ",a[8])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")


p1 = True

while(True):
    print_board()

    if p1:
        p = input("player 1,choose your place: ")
        if p in a:
            a[int(p)-1] = 'x'
            p1 = not p1

    else:
        p = input("player 2,choose your place: ")
        if p in a:
            a[int(p)-1] = 'o'
            p1 = not p1
    for i in range(3):
        if(a[i] == a[i+3] and a[i] == a[i+6]):
            print(a[i],"wins!!!")
            print("game over!!!")
            print_board()
            exit()
    for i in (0,3,6):
        if(a[i] == a[i+1] and a[i] == a[i+2]):
            print(a[i],"wins!!!")
            print("game over!!!")
            print_board()
            exit()
        if(a[0]==a[4] and a[0]==a[8]):
            print(a[0],"wins!!!!")
            print_board()
            exit()

        if(a[2]==a[4] and a[2]==a[6]):
            print(a[0],"wins!!!!")
            print_board()
            exit()
        else:
            print("invalied place!!!!!")
        
     

    










