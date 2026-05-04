#capgemini 2024
maths = ["Raj", "Anu", "Kiran", "Bala", "Pavi"]
political = ['Raj', 'Bala', 'Meera', 'Peter', 'Ken']
social = ['Ben', 'Raj', 'Meera', 'Arun', '']

# Remove empty values (important)
social = [x for x in social if x]

# Convert to sets
m = set(maths)
p = set(political)
s = set(social)

# All three
all_three = m & p & s

# Exactly two
exactly_two = (m & p) | (p & s) | (m & s)
exactly_two = exactly_two - all_three

# Only one
all_people = m | p | s
only_one = all_people - exactly_two - all_three

print("Only one subject =", list(only_one))
print("Exactly two subjects =", list(exactly_two))
print("All three subjects =", list(all_three))

######################----------------------------######################
maths = ["Raj", "Anu", "Kiran", "Bala", "Pavi"]
political = ['Raj', 'Bala', 'Meera', 'Peter', 'Ken']
social = ['Ben', 'Raj', 'Meera', 'Arun', '']

# Remove empty values (important)
social = [x for x in social if x]

m=set(maths)
p=set(political)
s=set(social)

#3 sub
print(list(m&p&s))

#2 sub
print(list(((m & p) | (p & s) | (m & s)) - (m & p & s)))

#1 sub
print(list((m | p | s) - ((m & p) | (p & s) | (m & s))))

##################################################################

import math

x = int(input("enter x :"))
y = int(input("enter y :"))
z = int(input("enter z :"))

if y >= x:
    print(1)
elif y <= z:
    print(-1)
else:
    cycles = math.ceil((x - y) / (y - z))
    minutes = cycles * 2 + 1
    print(minutes)

######################----------------------------######################
import math

x = int(input("enter x :"))
y = int(input("enter y :"))
z = int(input("enter z :"))
time=0
ht=0
i=1
while ht<x:
    if i%2==1:
        ht = ht+y
    else:
        ht=ht-z
    i=i+1
    time=time+1
print(time)

#---- will fail if y<=z -----#

##################################################################

#leap year or not 
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

##################################################################
#leetcode 412

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

#if i % 3 == 0 and i % 5 == 0: increment by 1 extra mod operation -> 15 because 15=3*5 and 3 and 5 are coprime GCD-->1
#if not a coprime use lcm ex: 4,6 -> lcm=12 

##################################################################

#string compression ----> aaabbbcccddaa -> a3b3c3d2a2

s = input("Enter the String : ")
res = ""
c = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c = c+1
    else:
        res = res + s[i - 1] + str(c)
        c = 1
res = res + s[-1] + str(c)
print("String Compression : ", res)


##################################################################

a = [2, 3, 4, 5]
b = a

a.append(10)
print(b)

b.append(200)
print(a)

# b = a  → both variables point to the SAME list in memory

# a ─┐
#    ├──> [2, 3, 4, 5]
# b ─┘

# b = a.copy()

# a ───> [2, 3, 4, 5, 10]
# b ───> [2, 3, 4, 5]

##################################################################
