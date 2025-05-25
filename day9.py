
#-------------------------- methods in list --------------------
# li=[]
# li.append(10)
# li.append([10,20])
# li.append((30,40))
# # li.append(10,20)# Error bcz only one element should be append at a time
# print(li)


# li=[10,20,30,40,30]
# li.pop(1)
# li.remove(30) # remove first occurrence of 30
# li.insert(1,100) # insert the element by passing index and value
# li.extend([60,70,80,90]) # the elements in a list added to the list. Here only sequential data type accepted
# print(li)
# li.reverse() # reverse the existing list
# print(li)

# li=[]
# for i in range(5):
#     l=int(input(f"enter a element {i+1}:"))
#     li.append(l)
# print(li)

# li=[1,2,3,4,5]
# pos=int(input('enter a position to insert:'))
# val=int(input("enter a element to insert:"))
# li.insert(pos-1,val)
# print(li)

# li=[1,2,3,4,5]
# ele=int(input('enter a element to delete:'))
# if ele in li:
#     li.remove(ele)
# else:
#     print(ele,'is not present in a list')

# li=[1,2,3,4,5]
# p=int(input("enter a position to delete element:"))
# if p in range(len(li)):
#     li.pop(p)
# else:
#     print('position not valid')
# print(li)

# li=[1,2,3,4,5]
# e=int(input("enter the element to know the pos:"))
# if e in li:
#     print(li.index(e))
# else:
#     print("element not found")

#--------------------methods in tuple ------------------

# tu=(1,2,3,4,5)
# elem=int(input("enter a element whose index has to be determined:"))
# if elem in tu:
#     print("The index of ",elem,"is",tu.index(elem))
# else:
#     print(elem,"is not found in tuple")

# ------------------- methods in sets ------------------------------

# s=set()
# print("enter a element:")
# for i in range(5):
#     n=int(input())
#     s.add(n)
# print(s)

# s={1,2,3,4,5,5}
# d=int(input('Enter the element to be deleted:'))
# if d in s:
#     s.remove(d)
#     print(d,'is deleted')
# else:
#     print("element not found")
# print(s)

# p=int(input('Enter the element to know the position:'))
# if p in s:
#    ---------- indexing is not possible in sets --------


# --------------------- methods in dictionary ------------------

dic={ }
name=input("enter a name:")
email=input("enter a email:")
mobile=int(input("enter a phno:"))
city=input("enter a city:")
pin=int(input("enter a pin:"))
dic['name']=name
dic['email']=email
dic['mobile']=mobile
dic['city']=city
dic['pin']=pin

# dic={
#     'name':name,
#     'email':email,
#     'mobile':mobile,
#     'city':city,
#     'pin':pin
# }

for i,j in dic.items():
    print(i,"=",j)

# n=input("enter new name to update:")
# dic.update(name=n)
#or dic['name']=n
# for i,j in dic.items():
#     print(i,"=",j)

# k=input("enter a key that u want to remove:")
# if k in dic.keys():
#     dic.pop(k)
#     for i, j in dic.items():
#         print(i, "=", j)
# else:
#     print("key not exists")


# v=input("enter a value to check whether exists or not:")
# if v.isdigit():
#     v=int(v)
# if v in dic.values():
#     print(v,"is found")
# else:
#     print(v,'not found')

# dic['state']=input("enter a state:")
# for i,j in dic.items():
#     print(i,"=",j)






