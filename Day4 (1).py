a=[11, 13, "Raju", 8.5]
print(a)

a = [ [2,3,4], [10,11,12], [44,55,6]]
print(a[1][1])


#####################################################################

#comprehension
a=[i for i in range(10,200)]
print(a)

# Ato Z
a=[chr(i) for i in range(65,91)]
print(a)

a=[chr(i) for i in range(65,91) if chr(i) not in "AEIOU"]
print(a)

#a to z
a=[chr(i) for i in range(97,123)]
print(a)

a=[chr(i) for i in range(97, 123) if chr(i) not in "AEIOU"]
print(a)

#####################################################################
#type casting  
#find max of the number

a=6789
b=[int(i) for i in str(a)]
print(max(b))

#####################################################################

names = ["WarrIor", "lAx", "LPs", "AkI","PiN"]
marks = [[90,60,50],[90,90,90],[20,30,50],[10,30,20],[20,90,30]]
b=1
for i in range(5):
    if sum(marks[i])/3 >=30 and sum(marks[i])/3 <49:
        print("{}. {} has scored {:.2f}% - {} Grade".format(b,names[i].capitalize(),sum(marks[i])/3, "C"))
    elif sum(marks[i])/3 >=50 and sum(marks[i])/3 <69:
        print("{}. {} has scored {:.2f}% - {} Grade".format(b,names[i].capitalize(),sum(marks[i])/3, "B"))
    elif sum(marks[i])/3 >=70:
        print("{}. {} has scored {:.2f}% - {} Grade".format(b,names[i].capitalize(),sum(marks[i])/3, "A"))
    else:
        print("{}. {} has scored {:.2f}% - {} Grade".format(b,names[i].capitalize(),sum(marks[i])/3, "F"))
    b=b+1

#####################################################################

names=["Rock Star","mallApur don","siddaARth","SIDDU","rahul model"]
marks=[[55,65,78],[86,98,56],[44,56,69],[65,78,86],[89,65,44]]
pos=1
g="F"
for i in range(5):
    b=sum(marks[i])//3
    if b>90:
        g="O"
    elif b<40:
        g="F"
    elif b>40 and b<60:
        g="B"
    else:
        g="A"
    print("{}.Mr/Mrs {} has scored = {:.2f}% Grade {}".format(pos,names[i].capitalize(),sum(marks[i])/3,g))
    pos=pos+1   

#####################################################################


#zip
names = ["rahul","sachin","sourav","yuvraj","kapil"]
age = [34,21,31,29,35]
res=list(zip(age,names))
pos=1
for i in res:
    print("Rank {} : Name {} is {} years old".format(pos, i[1].capitalize(),i[0]))
    pos=pos+1

################################################################
    
import random
a = int(input("Enter No of teams : "))
teams = []
print("Enter all team names : ")
for i in range(a):
    t=input("team name : ")
    teams.append(t)
m = int(input("Enter meet btw team : "))
matches=[]
for i in range(0,a-1):
    for j in range(i+1,a):
        for k in range(m):
            matches.append([teams[i],teams[j]])
pos=1
random.shuffle(matches)
for i in matches:
    print("Match No. {} : {} vs {}".format(pos,i[0],i[1]))
    pos +=1

################################################################
import random
from datetime import date, timedelta
a = int(input("Enter No of teams : "))
teams = []
print("\n *-------Enter all team names-------*\n")
for i in range(a):
    t=input("team name : ")
    teams.append(t)
m = int(input("Enter meet btw team : "))
print()
matches=[]
for i in range(0,a-1):
    for j in range(i+1,a):
        for k in range(m):
            matches.append([teams[i],teams[j]])
pos=1
random.shuffle(matches)
d=date.today()
print("\n *-------Total Matches-------*\n")
for i in matches:
    t = d + timedelta(days=pos)  
    print("Match No. {} : Date {} ----> {} vs {}".format(pos,t.strftime("%d/%m/%Y"),i[0],i[1]))
    pos +=1

########################################################################################

