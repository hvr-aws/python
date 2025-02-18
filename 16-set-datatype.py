"""
    Set is represented as {}
    it is defined in {}
    all the elements that are present inside set are unique.
    all the elements inside a set should be immutable
    set is a mutable datatype it can perform add update and delete.
    unordered: it does not support indexing
    slicing is also not possible
"""

a={1,2,4,6,7,9,7,4,2,3,9}
print(a)
#output: {1, 2, 3, 4, 6, 7, 9}

"""union"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.union(s2)
print("s3:",s3) 
#output: s3: {70, 40, 10, 80, 50, 20, 60, 30}


"""Intersection"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.intersection(s2)
print("s3:",s3)
#output: s3: {40, 50}


"""difference"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.difference(s2)
print("s3:",s3)
#output: s3: {10, 20, 30}

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s2.difference(s1)
print("s3:",s3)
# output: s3: {80, 60, 70}


"""symmetric_difference"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.symmetric_difference(s2)
print("s3:",s3)
#output: s3: {80, 20, 70, 10, 60, 30}


"""update"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s1.update(s2)
print(s1)
#output: {70, 40, 10, 80, 50, 20, 60, 30}

"""intersection_update"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s1.intersection_update(s2)
print(s1)
#output: {40, 50}


"""difference_update"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s1.difference_update(s2)
print(s1)
#output: {20, 10, 30}

""""deleting"""

"""1.pop()"""

a={1,2,3,4,5,6}
r=a.pop()
print(a,r)
  

"""2.remove()"""

a={10,20,30,40,50}
r=a.remove(30)
print(a,r)


a={10,20,30,40,50}
#r=a.remove(300)     #keyerror becoz element is not present in the set
#print(a,r)

"""3.discard()"""

a={5,6,7,8,9}
r=a.discard(9)
print(a,r)


a={5,6,7,8,9}
r=a.discard(300)
print(a,r)


a={1,2,2,3,4,5,6,6,7}
print(a,type(a))

"""add()"""

a={10,20,30,40,50}
a.add(60)
print(a)


a={10,20,30,40,50}
a.add(10)
print(a)