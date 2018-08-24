#1
a={}
for i in range(1,5):
    k=input("enter the key")
    v=int(input("enter a value"))
    a[k]=v
print(a)

#2
dic1={}
for i in range(2):
    stu=input("enter  name")
    for j in range(2):
        sub=input("enter subject ")
        marks=input("enter marks")
        
        dic1[stu,sub]=[sub,marks]
name=input("enter name")
for j in dic1.items():
    for r in range(2):
        if(j[r][0]==name):
            print(j[1])

