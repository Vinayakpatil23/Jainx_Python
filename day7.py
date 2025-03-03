
# li=[10,20,55,-2,0]
# biggest=0
# for i in li:
#     if i>biggest:
#         biggest=i
# print('biggest value in a lis id',biggest)
#
# smallest=biggest
# for j in li:
#     if j<smallest:
#         smallest=j
# print('smallest value in a list',smallest)
#
# smallest=li[0]
# for j in li:
#     if j<smallest:
#         smallest=j
# print('smallest value in a list',smallest)

# ----------------------------- loops with dictionary ------------

di={
    'x':10,
    'y':20
}

# for i in di:
#     print(i,di[i])

# for i,j in di.items():
#     print(i,j)

# for i in di.keys():
#     print(i)

# for i in di.values():
#     print(i)

# for i ,j in di.items():
#     print(i,'=',j)


# h_no=int(input('Enter teh house number:'))
# s=input('Enter the street name:')
# c=input('Enter the city:')
# p=int(input('Enter the pincode'))
# di ={
#     'house_no':h_no,
#     'street':s,
#     'city':c,
#     'pincode':p
# }
# for i,j in di.items():
#     print(i,j)

# li=[]
# n=int(input('enter a no of elements:'))
# for i in range(n):
#     num=int(input("enter a element"))
#     li.append(num)
# print(li)

n=int(input('enter a no:'))
t=n
while t>0:
    r=t%10
    t=t

