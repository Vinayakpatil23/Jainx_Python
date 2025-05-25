# li=[]
# for i in range(0,101,2):
#     li.append(i)
# print(li)


'''
li=[1,5,6,8,3]

#1->
x=[li[i]**2 for i in range(5) if i%2==1]
print(x)

#---- or ------
a=[]
for i in range(1,5,2):
    a.append(li[i]**2)
print(a)

#2->
y=[li[i]*5 for i in range(5) if i%2==0]
print(y)
#--- or --
b=[]
for i in range(0,5,2):
    b.append(li[i]*5)
print(b)

#3->
z=[li[i]*2 for i in range(5)]
print(z)
#---- or ---
c=[]
for i in range(5):
    c.append(li[i]*2)
print(c)
'''

'''
li=[11,3,6,10,13]
x=[li[i]**2 for i in range(5) if li[i]%3==0]
print(x)

#---------or --------
a=[]
for i in range(len(li)):
    if li[i]%3==0:
       a.append(li[i]**2)
print(a)

y=[i+5 for i in li]
print(y)
#---- or --
b=[]
for i in li:
       b.append(i+5)
print(b)

z=[li[i]**2 for i in range(5) if li[i]%3!=0]
print(z)
'''


# find word score and store it in dictionary
# x=['hi','python','we','write','python','we','say','hi','pyhon']
# d={}
# for i in x:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# x=[('a',10),('b',20),('c',30),('d',40)]
# y=dict(x)
# for i in y.values():
#     print(i,end=' ')
# --- or ---
# for i in x:
#     print(i[1],end=" ")

# x=['a','b','c','d']
# y=[10,20,30,40]
# d={}
# for i in range(4):
#     d[x[i]]=y[i]
# print(d)

# x=['a','b','c','d']
# y=[10,20,30,40]
# z=[(x[i],y[i]) for i in range(len(x))]
# print(z)

# ------------- globals() functions ----------

# x=10
# def f1():
#     x=20
#     print(x)
#     print(globals() ['x'])
# f1()

# x=10
# y=20
# def f1():
#     y=30
#     print(x)
#     print(y)
#     print(globals() ['x'])
#     print(globals() ['y'])
# f1()





