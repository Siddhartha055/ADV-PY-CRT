# try and error 
#nesting looping 


# heads = int(input("Enter total heads: "))
# legs = int(input("Enter total legs: "))

# # try all possibilities
# for hens in range(heads + 1):
#     cows = heads - hens
    
#     if (2 * hens + 4 * cows) == legs:
#         print("Hens:", hens)
#         print("Cows:", cows)
#         break
# else:
#     print("No solution found")

#####################################

# heads = int(input("Enter total heads: "))
# legs = int(input("Enter total legs: "))
# flag = False

# for cows in range(0,heads + 1):
#     hens = heads - cows
    
#     if (2 * hens + 4 * cows) == legs:
#         flag = True
#         break

# if flag:
#     print("Hens:", hens)
#     print("Cows:", cows)
# else:
#     print("No solution found")

#####################################

# import calendar

# year = int(input("Year: "))
# month = int(input("Month: "))
# print(calendar.month(year, month))

#####################################

# from datetime import date
# a = date(2005,2,2)
# b = date(2026, 4, 28)
# print(b-a)

#####################################

# from datetime import date

# y1, m1, d1 = map(int, input("Enter date1 (YYYY MM DD): ").split())
# y2, m2, d2 = map(int, input("Enter date2 (YYYY MM DD): ").split())

# a = date(y1, m1, d1)
# b = date(y2, m2, d2)

# print("Days:", (b - a).days)

#####################################

# from datetime import datetime

# y1, m1, d1, h1, min1 = map(int, input("Enter datetime1 (YYYY MM DD HH MM): ").split())
# y2, m2, d2, h2, min2 = map(int, input("Enter datetime2 (YYYY MM DD HH MM): ").split())

# a = datetime(y1, m1, d1, h1, min1)
# b = datetime(y2, m2, d2, h2, min2)

# diff = b - a

# print("lived days : ",diff.days,"seconds : ", diff.seconds)

#####################################

# a=2
# for i in range(2,5):
#     a=a+2
#     for j in range(4):
#         a=a+3
#     print(a)

# a = 10 
# for i in range(4):
#     for j in range(i+1):
#         a=a+i
#     print("ACE")
# print(a)
        
#####################################

# 3d prime number 

# c=0
# for i in range(100,1000):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         c=c+1
#         print(i, end=" ")
# print("\n total primes from 100 to 1000 are ",c)

#####################################

# a = int(input("col: "))
# while True:
#     b = int(input("row : "))
#     for i in range(b):
#         for j in range(a):
#             print("*",end=" ")
#         print()
#     print("Totle: " ,a*b)
#     print("--------------------------")

# a = int(input("col: "))
# b = int(input("row : "))
# c = int(input("loop : "))
# while c!=0:
#     for i in range(b):
#         for j in range(a):
#             print("*",end=" ")
#         print()
#     print("Totle: " ,a*b)
#     print("--------------------------")
#     c=c-1
#     b=b-1

#####################################