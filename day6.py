# --------------- for loop ----------------

'''
li=[10,20,30,40]
for i in li:
    print(i,end=' ')
'''
from traceback import print_tb

'''
li=[10,20,30,40,50]
for i in range(len(li)-1,-1,-1):
    print(li[i],end=' ')
'''
# output===50 40 30 20
'''
li=[10,20,30,40,50]
for i in range(0,len(li),2):
    print(li[i],end=' ')
'''

'''
li=[10,20,30,40,50]
for i in range(len(li)-2,0,-2):
    print(li[i],end=' ')
'''

'''
li=[10,20,13,61,50]
print('elements at even indices are:')
for i in range(0,len(li),2):
        print(li[i],end=' ')

li=[10,20,13,61,50]
print('elements at odd indices are:')
for i in range(1,len(li),2):
        print(li[i],end=' ')
'''

'''
li=[10,20,13,61,50]
for i in li:
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')
'''

'''
li=[10,20,13,61,50]
sum=0
for i in li:
    sum=sum+i
print('sum of elements is',sum) 
'''

# --------------------- sum of even and odd elements --------------------------
'''
li=[10,20,13,61,50]
sum=0
sum1=0
for i in li:
    if i%2==0:
        sum=sum+i
    else:
        sum1=sum1+i
print('sum of even elements',sum)
print('sum of odd elements',sum1)

# -------------------------- sum of even and odd indices -------------------------
li=[10,20,13,61,50]
sum=0
for i in range(0,len(li),2):
        sum=sum+li[i]
print('sum of even indices elements',sum)
sum1=0
for i in range(1,len(li),2):
        sum1=sum1+li[i]
print('sum of even indices elements',sum1)

'''

#---------------------- HW ------------------------------

# s=input('enter a string:')
# c=0
# for i in range(len(s)):
#     if s[i]==' ':
#         c=c+1
# print('no of words are:',c+1)
# print('no of spaces are',c)

# st=input('enter a string:')
# sc=0
# wc=0
# for i in st:
#     if i==' ':
#         sc=sc+1
# wc=sc+1
# print('word count',wc)
# print('space count',sc)

# vowels=['a','e','i','o','u',]
# c=input('enter a character:').lower()
# for i in range(len(vowels)):
#     if c==vowels[i]:
#         print(f'{c} is vowel')
#         break
#     else:
#         print(f'{c} is consonant')
#         break


# vowels=['a','e','i','o','u']
# c=input('enter a character:')
# for i in vowels:
#     if c == i:
#         print(f'{c}input is vowel')
#         break
#     else:
#         print('consonant')
#         break




