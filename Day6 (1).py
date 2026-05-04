## Function 
# inbuilt functions and userdefined functions
# ADV:- code reuse, readability, reduce code size, code-integration, 

#types of functions:-
#function without arguments and without return value

def h1():
    print("Hello World")
h1()

#function with arguments and without return value

def h2(a,b):
    print(a+b)
h2(1,2)

#function without arguments and with return value

def h4():
    return 23
print(h4())

#function with arguments and with return value

def h3(a,b):
    return a+b
print(h3(1,2))

############################################################################################

#1.area of square without arguments and without return
#2.area of rectangle without return and with arguments
#3.area of circle with return and without arguments
#4.area of triangle with return and with arguments
#5.enter your choice and call the function

def sq():
    a=int(input("Enter the value of side: "))
    print("Area of square: ",a*a)

def rect(a,b):
    print("Area of rectangle: ",a*b)

def circle():
    a=int(input("Enter the value of radius: "))
    return 3.14*a*a

def tri(a,b):
    return 0.5*a*b

while True:
    print()
    print("1.Area of square")
    print("2.Area of rectangle")
    print("3.Area of circle")
    print("4.Area of triangle")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        sq()
    elif choice==2:
        rect(int(input("Enter the value of length: ")),int(input("Enter the value of breadth: ")))
    elif choice==3:
        print("Area of circle : ",circle())
    elif choice==4:
        print("Area of Triangle : ", tri(int(input("Enter the value of base: ")),int(input("Enter the value of height: "))))
    elif choice==5:
        print("\n*-----------* Thank you *-----------*")
        break
    else:
        print("Invalid choice")

############################################################################################

def prime(n):
  if n <= 1:
    return False
  else:
    for i in range(2,n):
      if n % i == 0:
        return False
    return True
def sod(n):
  a = [int(i) for i in str(n)]
  s = sum(a)
  return s
def every(n):
  for i in range(3):
    s = n%10
    n = n // 10
    if not prime(s):
      return False
  return True

for i in range(100,1000):
  if prime(i) and prime(sod(i)) and every(i):
    print(i,end=" ")


############################################################################################

#return
def advbatch(n):
    for i in range(1,20):
        if i%n==0:
            return
        else:
            print("Ak")
    print("Are you okey ??")
advbatch(4)

#output: 
#Ak
#Ak
#Ak

#break
def advbatch(n):
    for i in range(1,20):
        if i%n==0:
            break
        else:
            print("Ak")
    print("Are you okey ??")
advbatch(4)

#output:
#Ak
#Ak
#Ak
#Are you okey ??

def advbatch(n):
    for i in range(1,20):
        if i%n==0:
            continue
        else:
            print("Ak")
    print("Are you okey ??")
advbatch(4)

#output:
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Ak
# Are you okey ??

############################################################################################

#pythogorase coprime triplet 

#method 1:
# def gcd(a,b):
#     while b!=0:
#         rem=a%b
#         a=b
#         b=rem
#     return a

#method 2:
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
    
def cop(i,j):
    return gcd(i,j)==1
    
a=int(input("Enter any num : "))
for i in range(5,a):
    for j in range(4,i):
        for k in range(3,j):
            if (i*i==j*j+k*k) and (cop(i,j) and cop(j,k) and cop(i,k)):
                print(i,j,k)


############################################################################################