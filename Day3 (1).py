#strings
#collection of char
#Immutable
#indexing and traversal 

a= "I love India 3000. india"

print(a[2:6])
print(a[2:])
print(a[:2])
print(a[::-1])

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.swapcase()) 
print(a.find("love")) #int output
print(a.find("loved")) #int output
print(a.count("love")) #int output
print(a.isupper()) #boolean output
print(a[13].isdigit()) #boolean output

c="qwerty"
print(c.isalpha())
b="909090"
print(b.isalnum())

print(a.split()) # return type list
print(a.split("India")) # return type list

print(type(a))
print(type(b))
print(type(c))

d=" ".join(c)
print(d)

a2="LALITH IS ALSO LPS"
e=" ".join(i for i in a2 if i in "AEIOU")
print(e)

a3="abcdefghi12345"
print(sorted(a3))


#password check 
# enter length between 7
# minimum one uppercase
# minimum one lowercase
# minimum one digit
# minimum one special char

a = input("Enter : ")
up = 0 
sm = 0 
nu = 0 
sp = 0

if len(a) > 7 and len(a.split())==1:
    for i in a:
        if i.isupper():
            up = up+1
        elif i.islower():
            sm =sm+1
        elif i.isdigit():
            nu = nu +1
        else:
            sp = sp+1
    if up > 0 and sp > 0 and sm > 0 and nu > 0:
        print("Strong")
    else :
        print("weak")
    
else:
    print("weak due to less character ")


#####################################################

# digital clock using while loop

import time
import sys
h=1
m=2
s=0
while True:
    sys.stdout.write("\r{h:02d}:{m:02d}:{s:02d}".format(h,m,s))
    sys.stdout.flush()
    time.sleep(1)
    s+=1
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
        h+=1
    if h==24:
        h=0

################################
# using pytz 
import time
import sys
import pytz
from datetime import datetime

ist = pytz.timezone("Asia/Kolkata")

while True:
    now = datetime.now(ist)
    h = now.hour
    m = now.minute
    s = now.second

    sys.stdout.write("\r{:02d}:{:02d}:{:02d}".format(h, m, s))
    sys.stdout.flush()
    time.sleep(1)


#all timezones

import time
import sys
import pytz
from datetime import datetime
a=pytz.timezone("Asia/Tokyo")
d=datetime.now(a)
print(d)
for i in pytz.all_timezones:
    print(i)

##################################
#palindrome

a=input("Enter : ").lower()
b="".join(i for i in a if i.isalnum() and i.isalpha())
c=b[::-1]
if b == c:
    print("YES")
else:
    print("NO")