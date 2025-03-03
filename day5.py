# ------------------ Greatest of two num -------------------------
'''
a=int(input('enter a num1:'))
b=int(input('enter a num2:'))
if a>b:
    print(a,' is greater than',b)
print(b,'is greater than ',a)
'''

#------------- among 3 values ------------------------------
'''
a=int(input('enter a num1:'))
b=int(input('enter a num2:'))
c=int(input('enter a num3:'))

if a>b and a>c:
    print(a,'is greater' )
elif b>c:
        print(b,'is greater')
else:
    print(c,'is greter')
'''

#-------------------------Even or Odd ---------------
'''
a=int(input('enter a num:'))
if a%2==0:
    print('even num')
else:
    print('odd')
'''

#---------------- vowel or consonant ------------
'''
s=input('enter a character:').lower()
if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
    print('the character is vowel')
else:
    print('the character is consonant')

'''

# ----------------------------leap year ---------------------------
'''
y=int(input('enter a year:'))
if y%400==0:
    print(y,'is a leap year')
elif y%4==0 and y%100!=0:
    print(y,'is a leap year')
else:
    print('not a leap year')

if y%400==0 or (y%4==0 and y%100!=0):
    print(y,'is a leap year')
else:
    print('not a leap year')
'''

#----------------------Palindrome -----------------------

'''
s=input("enter a string")
if s[: :-1].lower()==s.lower():
    print(s,'is palindrome')
else:
    print('not a palindrome')
'''


#------------------check weather fid square or not --------------

'''
l=int(input('enter a length:'))
b=int(input('enter a breadth'))
if l==b:
    print("square")
else:
    print("rectangle")
'''

#------------------ eligibility for admission -----------------------

'''
g=input('Enter a gender').lower()
h=int(input('enter a height'))
if g=='m':
    if h>=188:
        print(' male candidate eligible')
    else:
        print('not eligible')
elif g=='f':
    if h>=175:
        print(' female candidate eligible')
    else:
        print('not eligible')
else:
    print('not eligible')
'''

#-------------------------------while loop ---------------

# print A,C,E,G,H
'''
x=65
while x<=73:
    print(chr(x),end=' ')
    x=x+2
'''

#  ------------------- Tables 1 to 10----------------
'''
i=1
while i<=10:
    j=1
    while j<=10:
        print(f'{i}*{j}={i * j}')
        j=j+1
    i=i+1
'''

















