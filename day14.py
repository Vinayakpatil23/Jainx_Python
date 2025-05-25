# class Student:
#     def __init__(self,no,name,sub):
#         print("no is", no)
#         print("name is", name)
#         print("subject is", sub)
#         print()
#     def display(self,no,name,sub):
#         print("no is",no)
#         print("name is",name)
#         print("subject is",sub)
#
# o=Student(10,'vinay','CSE')
# o.display(20,'Raju','ECE')
from Tools.scripts.generate_opcode_h import internal_footer


# class Student:
#     def __init__(self, no, name, sub):
#         self.no=no
#         self.name=name
#         self.sub=sub
#
#     def display(self):
#         print("no is",self.no)
#         print("name is",self.name)
#         print("subject is",self.sub)
#
#
# o = Student(10, 'vinay', 'CSE')
# o.display()

# class Student:
#     def __init__(self, no, name, sub):
#         self.no=no
#         self.name=name
#         self.sub=sub
#
#     def display(self):
#         print("no is",self.no)
#         print("name is",self.name)
#         print("subject is",self.sub)
#         print()
# a=Student(1,'ramesh','python')
# a.display()
# b=Student(2,'suresh','django')
# b.display()
# c=Student(3,'mahesh','ml')
# c.display()

# z=40
# class Info:
#     y=20
#     print(z)
#     def m1(self):
#         print(Info.y)
#         self.x=10
#         print(self.x)
#
# i=Info()
# i.m1()
# print(i.y)

'''
class TypesMethod:
    def __init__(self):
        print("init method")

    def instance_method(self):
        print("instance method")

    @classmethod
    def class_method(cls):
        print("class method")

    @staticmethod
    def static_method():
        print("static method")

t=TypesMethod()
t.instance_method()
t.class_method()
# TypesMethod.class_method()
# TypesMethod.static_method()
t.static_method()
'''
'''
class A:
    x=10
    y=20

    def m1(self,x):
        self.z=30
        print(A.x)
        print(A.y)
        print(self.z)
        print(x)
        print()

    @classmethod
    def m2(cls,y):

        print(y)
        print(A.x)
        print(A.y)


o=A()
o.m1(40)
o.m2(40)
'''
lower=1
upper=10
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    # all prime numbers are greater than 1
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)