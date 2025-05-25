num=[]
n=int(input("enter a no of elements:"))
x=int(input("enter a x value:"))
y=int(input("enter a y value:"))
t=int(input("enter a t value:"))
c=0
for i in range(n):
    num.append(input("enter a element:"))
for i in range(t):
    for j in range(len(num)):
        a=num[i]+num[j]
        print(a)
        if x <= int(a) <= y:
            c+=1
print(c)