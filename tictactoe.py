import random

board = [" "," "," "," "," "," "," "," "," "," "]


def print_board():
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[1],"| ","    ",board[2],"    | ",board[3])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[4],"| ","    ",board[5],"    | ",board[6])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[7],"| ","    ",board[8],"    | ",board[9])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")


# x player 

while True:
    print_board()
    choice_x = int(input("please chose an empty slot for 'X'"))
    
    if(board[choice_x] == ' '):
        board[choice_x] ='x'
        print_board()        

    elif(board[1]=='x' and board[2]== 'x' and board[3]=='x'or
    board[4]=='x' and board[5]== 'x' and board[6]=='x'     or 
    board[7]=='x' and board[8]== 'x' and board[9]=='x'     or 
    board[1]=='x' and board[4]== 'x' and board[7]=='x'     or 
    board[2]=='x' and board[5]== 'x' and board[8]=='x'     or 
    board[3]=='x' and board[6]== 'x' and board[9]=='x'     or 
    board[1]=='x' and board[5]== 'x' and board[9]=='x'     or 
    board[3]=='x' and board[5]== 'x' and board[7]=='x'):
        print("x wins!!!")
        exit()

    else:
        print("sorry please select an empty slot for 'X'")

    choice_y = int(input("please chose an empty slot for 'o'"))
    if(board[choice_y] == ' '):
        board[choice_y] ='o'
        print_board()

    #cheack for o win  
    elif(board[1]=='o' and board[2]== 'o' and board[3]=='o' or 
        board[4]=='o' and board[5]== 'o' and board[6]=='o'  or 
        board[7]=='o' and board[8]== 'o' and board[9]=='o'  or 
        board[1]=='o' and board[4]== 'o' and board[7]=='o'  or 
        board[2]=='o' and board[5]== 'o' and board[8]=='o'  or 
        board[3]=='o' and board[6]== 'o' and board[9]=='o'  or 
        board[1]=='o' and board[5]== 'o' and board[9]=='o'  or 
        board[3]=='o' and board[5]== 'o' and board[7]=='o'):
        print_board()
        print("o wins!!!")
        exit()
           
    else:
        print("sorry please select an empty slot for 'o'")

   






    
