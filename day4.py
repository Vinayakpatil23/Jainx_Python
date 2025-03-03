def fun():  #---> defining a function
    print('hello')
fun() # ---->calling a function

# -----------------------------------------------------------------#
def details(x,y):
    print('name is ',x,' and location is ',y)
details('Vinayak','Bengaluru')

# -------------------------------------------------------------------#
# def arith(x,y):
#     print('sum=',x+y)
# a=int(input("enter a no:"))
# b=int(input("enter other no:"))
# arith(a,b)

#--------------------------------------------------------------------#

# s=input("enter a input string:")
# def reverse(s):
#     return (s[::-1])
# print(reverse(s))

# --------------------------------------------------------------------#

# def details(x,y):
#     return ('name is ',x,' and location is ',y)  #it will return in tuple format
# z=details('Vinayak','Bengaluru')
# print(z)

#----------------------------------------------------------------------#

# def details(x,y):
#     return f'{x},{y}'  # it will return in string format
# z=details('Vinayak','Bengaluru')
# print(z)

#-------------------------------------------------------------------#

def arith(x,y):
    return f'sum of {x} and {y} is {x+y}'
a=int(input("enter a no:"))
b=int(input("enter other no:"))
sum=arith(a,b)
# print('sum of ',a,'and ',b,'is',sum)
print(sum)