"""Dictionary is a mutable data type and we can dd, update and delete the elements 
   this is a unordered datatype and index can be anything and slicing is not supported

   a={"key" : "value"}
   a is a variable
"""
a= {"i am" : "Harsha"}
print(type(a)) # output : <class 'dict'>


# Accessing

a= {"course":"cloud"}
print (a["course"]) # output cloud

#printing dictionary

a={"name":["harsha", "chiuntu"], "gender": "male", "mail":["hvr@gmail.com", "hv9160@gmail.com"]}
print(a) # o/p: {'name': ['harsha', 'chiuntu'], 'gender': 'male', 'mail': ['hvr@gmail.com', 'hv9160@gmail.com']}

# appending
a= {"name":["hvr","msd","chh"]}
a["name"].append("sai")
print(a) #o/p: {'name': ['hvr', 'msd', 'chh', 'sai']}

#updating

a={"name": ["haha","spectrum"]}
a["name"][0]="hvr"
print(a) #o/p: {'name': ['hvr', 'spectrum']}

a={"name": ["haha","spectrum","msd", "tri"]}
a["name"][3]="hvr"
print(a) #o/p: 'name': ['haha', 'spectrum', 'msd', 'hvr']}

#adding a dictionary to others

a={"name":["adhahaha", "harsha"]}
a["gender"]={"male"}
a["id"]={1,2,3,4}
print(a) #{'name': ['adhahaha', 'harsha'], 'gender': {'male'}, 'id': {1, 2, 3, 4}}


# printing or accessing a value using get keyword
a={"name": {"hvr", "sai", "hn"}}
print(a.get("name")) # {'hn', 'sai', 'hvr'}


# None output
a={"name": "hvr"}
print(a.get("nam")) #o/p: hvr


# set default

a={"name":["haha", "hehe", "neeee"], "id":[1,2,3], "course":["python"]}

print(a.setdefault("country",["india"]))
print(a)



#problem statement
#create a dictionary with square of numbers from 0 to 10

squares = dict()
for num in range(1,11):
    squares.setdefault(num,num**2)
    print(squares)

# keys() values() items()

a={"x":[1,2,3,4], "y":[5,6,7,9]}
for ele in a:
    print(ele)

#output
#x
#y

a={"x":[1,2,3,4], "y":[5,6,7,9]}
for ele in a.values():
    print(ele)
"""
output
[1, 2, 3, 4]
[5, 6, 7, 9]
"""

a={"x":[1,2,3,4], "y":[5,6,7,9]}
for ele in a.items():
    print(ele) 
    # output 
    #('x', [1, 2, 3, 4])
    #('y', [5, 6, 7, 9])


"""
Deleting
   popitem
   pop
   del
   clear
"""

# popitem: delets last key value pairs in a dict()

test={"a":[2,4,6,8], "b":[1,3,5,7]}
match=test.popitem()
print(test,match)#output: {'a': [2, 4, 6, 8]} ('b', [1, 3, 5, 7])

# pop

test={"a":[2,4,6,8], "b":[1,3,5,7]}
match=test.pop("a")
print(test,match) #output: {'b': [1, 3, 5, 7]} [2, 4, 6, 8]


# Update

a={1:1,2:2,3:3}
b={2:4,6:6}
a.update(b)
print(a) #output: {1: 1, 2: 4, 3: 3, 6: 6}
a["new"]=b
print(a) # output: {1: 1, 2: 4, 3: 3, 6: 6, 'new': {2: 4, 6: 6}}

# celar(): removes everything in a directory
a= {1:1,2:2,5:6}
a.clear()
print(a) #output: {}

#delete (del) : delets an element from a directory

test={"a":[2,4,6,8], "b":[1,3,5,7]}
del test["a"]
print(test) #output; {'b': [1, 3, 5, 7]}

# zip(): method to access elements from 2 dict or lists at same time

a={1:1,2:2,3:3}
for x,y in zip(a.keys(), a.values()):
    print(x,y)
"""
output
   1 1
   2 2
   3 3
"""
a={"name":["haha", "hehe", "huhu"], "id":[22,33]}
for x,y in zip(a.keys(), a.values()):
   print(x,y)

"""
output
   name ['haha', 'hehe', 'huhu']
   id [22, 33]
"""

#copy:
a={1:1,2:2,3:3}
d2=a.copy()
print(a,d2)
#output: {1: 1, 2: 2, 3: 3} {1: 1, 2: 2, 3: 3}

d1={1:1,2:2,3:7}
d2=d1.copy()
d2[4]=16
print(d1,d2)
#output: {1: 1, 2: 2, 3: 7} {1: 1, 2: 2, 3: 7, 4: 16}





