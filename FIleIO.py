# f=open("Sample.txt",'w')
# f.write("This is simple file \n")
# f.close()
from dataclasses import replace

# f=open("Sample.txt",'r+')
# f.write("I am learning python")
# f.close()

# f=open("Sample.txt",'a')
# f.write("I am learning python")
# f.close()

# with open("Sample.txt") as f:
    # print(f.read())
    # print(f.readlines())
    # l1=f.readline()
    # print(l1)
    # l2 = f.readline()
    # print(l2)

f=open("Info.txt",'w')
f.write("I am Vinayak Veeranagouda Patil ")
f.write("\nI am learning Python")
f.close()

f=open("Info.txt","a")
f.write("\nI am from Govt sksjti college\n")
f.write("My USN is 1sk21cs054")
f.close()


f=open("Info.txt",'r')
res=f.read()
content=res.replace("Vinayak Veeranagouda", "vinayak")
f.close()


f=open("Info.txt",'w')
f.write(content)
f.close()