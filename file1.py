# a=10
# b=20
# f= a+b
# print(f)
#
# def add(c,s):
#     x = c+s
#     return x
#
# i= input("enter 1st number")
# j= input("enter 2nd number")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b

print("Calculator with your choice")

print("choose operation")
print("1:  Addition")
print("2:  Substruction")
print("3:   Division")
print("4:   Multiplication")
print("5:   Modulus")

choice = int(input("enter what operation you choose"))
if choice == 1:
    print(add(int(input("enter num1: ")),int(input ("enter num2: "))))
elif choice == 2:
    print(sub(int(input("enter num1: ")),int(input ("enter num2: "))))
elif choice ==3:
    print(divide(int(input("enter num1: ")), int(input("enter num2: "))))
elif choice==4:
    print(mul(int(input("enter num1: ")), int(input("enter num2: "))))
elif choice ==5:
    print(mod(int(input("enter num1: ")), int(input("enter num2: "))))
else:
    print("invalid choice")
