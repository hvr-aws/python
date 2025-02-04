"""represented with ()
supports insexing and slicing
"""
a=(10,22,33)
print(a[0])
print(a[1])
print(a[2])



""" 
insert value 40 at end of array 
tuple is an immutable because we cannot insert values to it
we need to change to list and insert
"""
a=(10,22,33)
a=list(a)
print(a)
a.append(40)
a=tuple(a)
print(a)

a,b=10,20
print(a)
print(b)

#enumerate

a=(12,34,45)

for idx,ele in enumerate(a):
    print(idx,ele)