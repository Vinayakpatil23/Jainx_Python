# class A:
#     x=10
# class B(A):
#     y=20
# print(B.y)

#--------------- inheritance----------
#single level
# class X:
#     x=10
#     def m1(self):
#         print("parent class")
# class Y(X):
#     y=20
#     def m2(self):
#         print("child class")
# o=Y()
# o.m1()
# o.m2()
# print(Y.x)
# print(Y.y)
# print(X.x)

#multilevel
# class X:
#     x=10
#     def m1(self):
#         print("parent class")
# class Y(X):
#     y=20
#     def m2(self):
#         print("child class")
# class Z(Y):
#     z=30
#     def m3(self):
#         print("sub child class")
# o=Z()
# o.m1()
# o.m2()
# o.m3()
# print(Z.x)
# print(Z.y)
# print(Z.z)

# Hierarchical Inheritance

# class A:
#     x=10
#     y=20
# class B(A):
#     z=30
# class C(A):
#     a=40
# c=C()
# print(c.y)
# print(c.x)
# b=B()
# print(b.x)
# print(b.y)

# Multiple Inheritance

# class A:
#     x=10
# class B:
#     y=20
# class C(A,B):
#     z=30
# c=C()
# print(c.y)
# print(c.x)
# print(c.z)

# Hybrid or dimond inheritance

# class A:
#     x=10
# class B(A):
#     y=20
# class C(A):
#     z=30
# class D(B,C):
#     k=40
# c=C()
# print(c.x)
# b=B()
# print(b.x)
# d=D()
# print(d.y)
# print(d.x)
# print(d.z)

# class A:
#     def __init__(self):
#         print("class A Constructor")
# class B(A):
#     def __init__(self,x):
#         super().__init__()
#         print("class B Constructor",x)
# class C(B):
#     def __init__(self):
#         super().__init__(10)
#         print("class C constructor")
# o=C()


class Student:
    def __init__(self,name,usn,marks):#or *marks
        self.n=name
        self.u=usn
        self.m=marks

    def calc_avg(self):
        total=0
        # for i in range(len(self.m)):
        #     total=total+int(self.m[i])
        for i in self.m:
            total+=i
        return total//3

    # def display_grade(self,a):
    #     if a>=90:
    #         print("A")
    #     elif a>=75 and a<90:
    #         print("B")
    #     elif a>=50 and a<75:
    #         print("C")
    #     else:
    #         print("F")

    def display_grade(self):
        if self.calc_avg()>=90:
            print("A")
        elif self.calc_avg()>=75 and self.calc_avg()<90:
            print("B")
        elif self.calc_avg()>=50 and self.calc_avg()<75:
            print("C")
        else:
            print("F")

o=Student("vinayak","1sk21cs054",[50,50,90])
a=o.calc_avg()
o.display_grade()
