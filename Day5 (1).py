#leetcode 1480
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums

#########################################################

a = [[" " for i in range(11)] for i in range(11)]

for i in range(11):
    for j in range(11):
        if j == 0:
            a[i][j] = "*"
        elif j == 11 - 1:
            a[i][j] = "*"
        elif i == j and i <= 11 // 2:
            a[i][j] = "*"
        elif i + j == 11 - 1 and i <= 11 // 2:
            a[i][j] = "*"
for row in a:
    print(*row)


##################################################################
a={}
print(type(a))
#output  -> <class 'dict'>

##################################################################

a={2,2,3,4,5,6,5,6}
for i in a:
    print("HI")
#output -> HI HI HI HI HI HI (6 times) no duplicates

##################################################################

#set operations

a={23,4,5,6}
b={23,5,6,7,9}
print(a.union(b))
print(a&b) #intersection
print(a^b) #non intersection
print(a-b) #non common
print(a|b) # union


print()
a.add(99)
print(a)
a.remove(99)
print(a)

##################################################################

#dictionary

d={'name':'Rahul', 234:[1,2,3,4,5],'Runs':4000} 
d["dept"]='AIM'
# for i in d.keys():
#     print(i)
# print()
# for i in d.values():
#     print(i)
# print()
# for i in d.items():
#     print(i)
print(d)


##################################################################
# round or not round number 
# first starting with any positive integer
# replace the number with sum of its digits
# repeat till the number equal to 1
# check whether the number is round or not round

a=int(input("Enter a number: "))

if a<0:
    a=-a
    
while a>=10:
    sum_digits = 0
    for i in str(a):
        sum_digits += int(i)
    a = sum_digits

if a==1:
    print("Round number")
else:
    print("Not a round number")
    
##################################################################
#round or not round number - II

a=int(input("Enter a number: "))
nums = []
while True:
    if a==1:
        break
    elif a in nums:
        break
    else:
        nums.append(a)
        d=sum([int(i)*int(i) for i in str(a)])
        nums.append(d)
        a=d

if  a==1:
    print("Round number")
    print(nums)
else:
    print("Not a round number")
    print(nums)


##################################################################