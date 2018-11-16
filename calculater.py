def sum(num1,num2):
    return num1 + num2
def subract(num1,num2):
    return num1 - num2
def dev(num1 , num2):
    return num1 / num2
def mult(num1 , num2):
    return num1 * num2
print("---------------------------------------------------------")
print("what's your choice??")
print("1 for add")
print("2 for sub")
print("3 for dev")
print("4 for mult")

choice = input("text your choice?  :")
num1 = int(input("input first number  :"))
num2 = int(input("input secont number :"))

if choice == "1":
    print(sum(num1,num2))
elif choice == "2":
    print(subract(num1,num2))
elif choice == "3":
    print(dev(num1,num2))
elif choice == "4":
    print(mult(num1,num2))
else:
    print("enetre a valied number")
