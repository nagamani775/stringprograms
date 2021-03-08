s=input("enter the string")
s1=s.split()
print(s1)
#1st method using reversed method
#r=reversed(s1)
#output=''.join(r)
#print(output)
s2=s1[::-1]
print(s2)
output=' '.join(s2)
print(output)