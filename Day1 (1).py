## loops in python

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# #################
# for i in range(10):
#     print("*", end=" ")
# print()

# for i in range(10):
#     print("*                 *")

# for i in range(10):
#     print("*", end=" ")
# print()

# ###########################
# while True :
#     n=int(input("enter:"))
#     if(n%2==0):
#         for j in range(1,11):
#             # print(j,"*",n,"=",n*j)
#             print("{} x {} = {}".format(j,n,j*n))
#         print()
#     else:
#         for j in range(1,n+1):
#             # print(j,"*",n,"=",j*n)
#             print("{} x {} = {}".format(j,n,j*n))
#         print()

# ###########################

# s = input("Please enter sentence: ")
# count = len(s.split())
# print(f"The number of words is: {count}")   

# import re
# s = input("Please enter sentence: ")
# words = re.findall(r'\b\w+\b', s)
# count = len(words)
# print(f"The number of words is: {count}")   

# s = input("Please enter sentence: ")
# count = 0
# in_word = False

# for char in s:
#     if char == ' ':
#         in_word = False
#     elif not in_word:
#         count += 1
#         in_word = True

# print(f"The number of words is: {count}")   

# ###########################








