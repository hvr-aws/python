"""
list
list is a heterohenous data type holds any data
using list we can store multiple values in a variable
eg: a=[1,2,3,4,5,2]
"""
a=[2,3,5,7,"harsha",6, True ]
print(a)


"""
indexing
accessing elements inside a variable and elements position inside a variable
"""
a=[2,3,5,7,"harsha",6, True ]
#print(a[9])
print(a[3])


"""
How to find length of a list
"""
a=[2,3,5,7,"harsha",6, True ]
print("length of list is: ", len(a))



"""
Slicing operation in list
output: [0, 5, 7, 8]
"""
a=[0,5,7,8,3,4,8,9]
print("output is : ",a[0:4])

"""fetching all that are at even positions"""
a=[0,5,7,8,3,4,8,9]
print("even positions are: ",a[::2])

"""fetching all that are at odd positions"""
a=[0,5,7,8,3,4,8,9]
print("odd positions are :",a[1::2])   

"""Reversing a list"""
a=[0,5,7,8,3,4,8,9]
print("after Reversing a list is: ",a[::-1])

"""Appending or extending: 
Adds the element at the end of the list only"""
a=[20,4,5,79,88,1]
a.append(143)
a.append(234)
print(a)

"""How to insert element as per user choice"""

a=[20,4,5,79,88,1]
a.insert(0,22)
print(a)

"""How to Update an element in a list"""
a=[20,4,5,79,88,1]
a[1]=77
print(a)

"""fetch the element 987 from the list"""

""" # a=[4,5,7,9,12[23,55,7,9[34,78[143,56,89]]]]

# print(a[5][4][2][3])
  """
print(a)

"""Deleting elements from a list
1. pop: removes element based on index
2. remove: removes elemenet based on value
3. clear: removes all the elements in a list and returs empty list
4. delete: removes all the references in the list"""
a=[12,33,44,55,66,56]
a.pop(1)
print(a)
a=[12,33,44,55,66,56]
a.remove(66)
print(a)
a=[12,33,44,55,66,56]
b=a.clear()
print(a)

"""
Sorting
How to sort a list
"""
#sort
a=[39,4,33,8,9,11]
a.sort()
print(a)

#sorted
a=[39,4,33,8,9,11]
b=sorted(a)
print(a)
print(b)

#Descending
a=[3,56,89,65,4,2]
b=sorted(a,reverse=True) #this works as a desending order
print(b)


a=[3,56,89,65,4,2]
b=sorted(a,reverse=False) #this works as ascending order
print(b)

"""Index of an element in a list"""

a=[10,20,30,77,59]
a_id= a.index(77)
print(a_id)

""" a=[10,20,30,77,59]
b= a.index(34) # gives as value not in list
print(b)
 """


#"""Count the occurances of an element in list"""

a=[22,44,77,95,22,55,44,67,44,77]
b=a.count(44)
print(b)

"""How to Add two lists"""

a=[20,30,55,77]
b=[34,5,6,7,8,9,99]
c=a+b
print(c)

"""Condition statement and loops
   Condition statement: <,>,>=,<=,==,!=    o/p: t/f
   variable should not be a keyword, we use if keyword

   if(condition):
   operation
   else
   operation
"""

a=22
b=33
if(a>b):
    print("a is grater")
else:
    print("b is grater")

"""if-elif-else"""

num1=345
num2=456
if(num1>num2):
      print("num2 is grater")
elif(num2>num1):
      print("num1 is smaller ")
else:
      print("both are equal")

"""how to know if an element is present in a list
  Method:1
"""
a=[22,33,55,77,88,12,567,987]
b=a.count(33)
if(b!=0):
      print("element exist")
else:
      print("element does not exist")

#methos2

a=[22,33,55,77,88,12,567,987]
b=2
c=a.count(b)
if(c!=0):
      print("element exist")
else:
      print("element does not exist")

#method3

a=[22,33,55,77,88,12,567,987]
b=33
print(b in a)

