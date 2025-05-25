# res= lambda n1,n2:n1+n2
# result=res(10,20)
# print(result)
from Tools.scripts.var_access_benchmark import list_append_pop

#string reverse
# rev=lambda s:s[::-1]
# res=rev('Vinayak')
# print(res)

#greatest of two no
# great=lambda a,b:a if a>b else b
# r1=great(100,20)
# print(r1)

#even or odd
# evenOdd=lambda x:'even' if x%2==0 else 'odd'
# r2=evenOdd(3)
# print(r2)

# def f1(revers,x):
#     print('function as a parameter')
#     print(revers(x))
# f1(rev,'hello')

# def f2(greatest,x,y):
#     print(greatest(x,y))
# f2(great,10,20)

#print odd numbers
# x=[10,11,12,13,14,15]
# for i in x:
#     if i%2!=0:
#         print(i)

# y=filter(lambda i:(i%2!=0),x)#<filter object at 0x00000234AB252D10>
# y=list(filter(lambda i:(i%2!=0),x))
# print(y)


#print double of each element
x=[10,5,6,8]
# for i in x:
#     print(i*2)

y=list(map(lambda i:i*2,x))
print(y)


