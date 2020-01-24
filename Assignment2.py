print("#################### ASSIGNMENT PIAIC BY SALMA_66197 ####################")
print("\n ################## FACTORIAL WITH FUNCTION AND SIMPLE IF ELSE LOOP ####################### \n")


#with function
print("######## WITH FUNCTION ########### \n")
def fact(n):
   if n==1:
    return n
   else:
    return n*fact(n-1)

n=int(input("enter number for factorial"))
if n<0:
   print("number is negative")
elif n==0:
   print ("0! is 1")
else:
   print("the num factorial is",fact(n))

#with if-else
print("\n ######## WITH If-Else ########### \n")

f=1 #set value of variable f
n=int(input("enter number")) #prompt user to enter number
if n<0: #if num is less than zero then print num is negative
    print("num is negative")
elif n==0: #if num =0 then print 0! is 1
    print("0! is 1")
else: #else done factorial using for loop
    for i in range(1,n+1): #start from 1 run untill n
        f=f*i #Multiply with i
    print("the factorial is ",f) #print factorial of number if for loop end


print("\n ################## FIND EVEN AND ODD NUM WITH FUNCTION AND SIMPLE IF ELSE LOOP ####################### \n")

print("\n ######## WITH If-Else ########### \n")
number = int(input("enter number: ")) #prompt user to enter num
if(number%2== 0): #if num mode 2 is equal to zero then even
    print("num is even")
else: #else odd
    print("odd number")


print("######## WITH FUNCTION ########### \n")
def func(n): #func with parameter n
    if n%2==0:
        print("Number is even")
    else:
        print("number is odd")
    return n

num = int(input("Enter number: "))
print(func(num))


print("\n ################## FIND PRIME NUMBER WITH FUNCTION AND SIMPLE IF ELSE LOOP ####################### \n")

print("\n ######## WITH If-Else ########### \n")

number = int(input("Enter any number: ")) #prompt user to enter number
# prime number is always greater than 1
if number > 1:
    for i in range(2, number): #for loop to check there is any pos divisor is available
        if (number % i) == 0:  #if any divisor  found of num it is not prime number
            print(number, "is not a prime number")
            break # use to come out of the loop as soon as any positive divisor is found as there is no further check is required
    else: #else num is prime number
        print(number, "is a prime number")

else: #prime num is always pos if line64 condition false then num is not prime number
    print(number, "is not a prime number")

print("\n ######## WITH FUNCTION ########### \n")

def Prime(n):
    if (n <= 1): #neg num not prime
        return "Not a Prime no"
    if (n <= 3):
        return "Prime Number"
    if (n % 2 == 0 or n % 3 == 0): #This is checked so that i skip middle five numbers in while  loop
        return "Not a Prime number"
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return "Not a prime num"
        i = i + 6
    return "Prime Number"

#calling function
p_num= int(input("enter a number: "))
print(Prime(p_num))

print("\n ################## CALCULATOR OF SIMPLE MATH OPERATION ####################### \n")
print("################## AND TO FIND AREA OF SQUARE,TRIANGLE,CIRCLE ####################### \n")


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
def square(a):
    return a*a
def triangle(u,v): #base * height divide by 2
    return (u*v)/2
def circle(r): #pie r^2
    pie = 3.1414
    return pie*r*r



print("\n Calculator with your choice")

print("choose operation")
print("1:  Addition")
print("2:  Substruction")
print("3:   Division")
print("4:   Multiplication")
print("5:   Modulus")
print("6:  Area of Square")
print("7:  Area of Triangle")
print("8:  Area of Circle")

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
elif choice == 6:
    print("Area of Square: ",square(int(input("enter num: "))))
elif choice == 7:
    print("Area of Triangle: ",triangle(int(input("base: ")),int(input ("height: "))))
elif choice ==8:
    print("Area of Circle: ",circle(float(input("radius: "))))
else:
    print("invalid choice")
