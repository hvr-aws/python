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