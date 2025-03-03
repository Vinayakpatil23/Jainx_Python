x=[1,2,3]
y=x*2
z=[i+1 for i in y]
print(z)

# li=['hello','good']
# s=set(li)
# print(s)
# s='morning'
# s[2]='k'
# print(s)//string do not allow index based operation,indexing but slicing allowed
# s='morning'
# print(s[::2])
# r=range(10,100,2)
# li=list(r)
# print(li)
# r=range(0,100,2)#even
# li=list(r)
# print(li)
# r=range(1,100,2)#odd
# li=list(r)
# print(li)
# r=range(5,55,5)
# li=list(r)
# print(li)
# r=range(100,-1,-2)
# li=list(r)
# print(li)
# r=range(99,0,-2)
# li=list(r)
# print(li)
# r=range(49,-24,-8)
# li=list(r)
# print(li)
# r=range(24,-1,-4)
# li=list(r)
# print(li)
# r=range(41,-10,-7)
# li=list(r)
# print(li)
# r=range(5,42,7)
# li=list(r)
# print(li)
# dictionary={
#     'name':'vinayak',
#     'age':22,
#     'loc':'bng',
#     'loc':'dvg'#if two keys are same it will replace with latest value
# }
# print(dictionary)
# print(dictionary['name'])
# dictionary['ph_no']=11111111
# print(dictionary)

x= {
    'eno':1,
    'ename':'vinayak',
    'esal':200000
}

x['esal']=50000

x['loc']='bng'
print(x)