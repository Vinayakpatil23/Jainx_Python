# def fun():
#     pass
# print(fun())

# i=1
# while i <=10 :
#     pass

# def fun(x,y):
#     print(x,y)
# fun(10,20)

# def fun(x,y):
#     print(x,y)
# fun(x=10,y=20)

# def fun(x,y):
#     print(x,y)
# fun(x=10,20) # Error

# def fun(x,y):
#     print(x,y)
# fun(10,x=20) # Error

# def fun(x,y,z=30):
#     print(x,y,z)
# fun(12,20)
# fun(10,20,50)

# def fun(*a):
#     print(a) # it will print in tuple
# fun(12,20)

# def fun(*a):
#     for i in a:
#         print(i,end=" ")
# fun(12,20,30)

# def fun(*args):
#     for i in args:
#         print(i,end=" ")
# fun('hello',30,50,'hi')

# def fun(x,*y,z=100):
#     print(x,y,z)
# fun(10,20,30,40,60)
# fun(10,20,30,40)
# fun(10,20,30,z=108)

# def fun(**kwargs):
#     for i,j in kwargs.items():
#         print(i,'=',j)
# fun(id=54,name='vinayak',loc='bengaluru',phno=733768)
#
# name=input("enter a patient name:")
# blood=input('enter blood group:')
# no=int(input("enter no diseases:"))
# diseases=input("enter a diseases:")
# diseases1=input("enter a diseases:")
# diseases2=input("enter a diseases:")
#
# email=input("enter a email:")
#
# def hospital(n,b,*d,e='not provided'):
#     print('name is ',n)
#     print('blood group is:',b)
#     print('diseases are:',d)
#     print('email is',e)
#
# hospital(name,blood,diseases,diseases1,diseases2,email)
# hospital('vinayak','O+ve','BP')
# hospital('vinayak','O+ve','BP','fever' , e='patil@123')