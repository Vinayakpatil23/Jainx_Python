# import calendar
# year=int(input("enter a year:"))
# month=int(input("enter a month:"))
# display=calendar.month(year,month)
# print(display)

# import datetime
# print(datetime.datetime.now())

# import math
# print(math.factorial(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")


# no=int(input('enter a no:'))
# fact=no
# for i in range(1,no):
#     fact=fact*i
# print("factorial is",fact)


# h=int(input("enter a height of triangle:"))
# l=int(input("enter a length of triangle:"))
# area=1/2*(l*h)
# print("area of triangle:",area)

# m=int(input("enter a distance in miles:"))
# km=1.6*m
# print(m," miles in km is",km)

# a=int(input("enter a no:"))
# b=int(input("enter other no no:"))
# print(" before swapping a =",a,"and b=",b)
# c=a
# a=b
# b=c
# print("after swapping a =",a,"b=",b)

# c=int(input("enter a temp in celsius:"))
# f=c*(9/5)+32
# print(f)

# n=int(input("enter a no:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")

# num=int(input("enter a num:"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

a=int(input("enter a 1 no:"))
b=int(input("enter a 2 no:"))
s=0
for i in range(a,b):
    s=s+i
print(s)

