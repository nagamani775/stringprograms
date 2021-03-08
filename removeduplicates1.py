s=input("enter the string")
l1=[]
for item in s:
    if item  not in l1:
        l1.append(item)

print(l1)