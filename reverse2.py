s=input("enter the string")
r=reversed(s)
print(type(r))#<class reversed> its an object
print(r)
#for ch in r:
 #   print(ch)

output=''.join(r)
print(output)