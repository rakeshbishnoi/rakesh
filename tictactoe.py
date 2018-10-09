
a=['1','2','3','4','5','6','7','8','9']

def printBoard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("------")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("------")
	print(a[6]+'|'+a[7]+'|'+a[8])
printBoard()

ply1 Turn = True

for i in range(9):
printBoard()
#ply1 plays
	if ply1 Turn:
		p = input("ply1,choose ur place:")
		if p in a:
			a[int(p)-1] = 'X'
			ply1 Turn = not ply1 Turn
#ply2 plays
	else:
		p = input("ply2, choose ur place:")
		if p in a:
			a[int(p)-1] = 'O'
			ply2 Turn = not ply2 Turn

check for winning condition
if(a=0)

print(a[0],a[1],a[2]) or (a[3],a[4],a[5]) or (a[6],a[7],a[8])
print(a[0],a[3],a[6]) or (a[1],a[4],a[7]) or (a[2],a[5],a[8])
print(a[0],a[4],a[8]) or (a[2],a[4],a[6])

#check for tie condition
elif(a=9):
print("tie")
