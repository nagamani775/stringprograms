s=input("enter the string")
s1=s.split()
print(s1)
l1=[]
for word in s1:
    l1.append(word[::-1])
print(l1)
output=' '.join(l1)
print(output)