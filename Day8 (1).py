""" 
Recursion :
        function calling itself
        base cond -> exit of fns
        arg : should be different
        ans of big prob in terms of small prob
        backtracking 
        nested recursion(more than one recursive call to itself)
"""

##########################################################################################
    
#fibonacci series

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

# n=int(input("enter a no"))
n=6
for i in range(n):
    print(fib(i),end=" ")

##########################################################################################

#backtracking:-
def f(a):
    if a==4:
        return
    print(a+10,end=" ")
    f(a+1)
    
    print(a,end=" ")
f(1)
#output
#11 12 13 3 2 1 

##########################################################################################

def f(a):
    if a==1:
        return
    a-=1
    f(a)
    print("help",end=" ")
    f(a)
    
f(int(input("enter the number : ")))

#output
#enter the number : 5
# help help help help help help help help help help help help help help help 

##########################################################################################

def f(a):
    if a==4:
        return 1
    a=f(a+1)
    print("hai",end=" ")
    return a+2
    
print(f(int(input("enter the number : "))))

#output
# enter the number : 1
# hai hai hai hai 9

##########################################################################################

# OOP's

"""
1, variable
2, function
3, class
4, object
5, method
6, constructor
7, inheritance
8, polymorphism


variable: 
    1, local variable -------------> (method variables // method has its own values)

    --------(global variable)----------

    2, class variable (or) static variable ----------> (class variables // each objects holders same value \ each object has same copy )
    3, instance variable ----------> (global variables // each objects holders unique value \ each object has separate copy )
    4, complete variable ------------> (every objects  )

Class : 
      container (methods and objects)
      user define data type
      blueprint

Object : 
      instance of a class

Attribute : 
      variables

Method : 
      functions

inside or out side the class the methode and var should be used or invoked  by ----> objects or class name 

"""


class abc:
    def set_dim(self, a, b):
        self.total=a+b
    def display(self):
        print("Add : ",self.total)

a=abc()
b=abc()
a.set_dim(20,30)
b.set_dim(30,50)
a.display()
b.display()

##########################################################################################

class ACE:
    col="ACE"
    def give_details(self,a,b,c,d):
        self.tot=a+b+c
        self.name=d
    def dis(self):
        print("1.Name : ",self.name)
        print("2.Marks : ",self.tot)
        print("3 Collage : ",ACE.col)
        # print("4 Country : ",x)

class bvrit:
    col="BVRIT"
    def give_details(self,a,b,c,d):
        self.tot=a+b+c
        self.name=d
    def dis(self):
        print("1.Name : ",self.name)
        print("2.Marks : ",self.tot)
        print("3.Collage : ",ACE.col)
        # print("4. Country : ",x)



a=ACE()
b=ACE()
a.give_details(1,2,3,"IND")
b.give_details(4,5,6,"NZ")
a.dis()
b.dis()
# print(a+b)

##########################################################################################
