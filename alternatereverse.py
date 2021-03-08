s=input("enter the string")
s1=s.split()
print(s1)
l1=[]
i=0
while i<len(s1):
    if i%2==0:
        l1.append(s1[i])
    else:
        l1.append(s1[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
