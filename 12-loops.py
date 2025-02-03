"""print the element along with its index in list

   length based loop
"""

fruits = ["apple", "banana", "mango", "orange"]

for idx in range(len(fruits)):
    print(idx, fruits[idx])

"""range based loop"""

a=[22,33,44,66,88,9,9,0,3,4,5,7,7,8]
for element in range (0,10,2):
        print(element)



#Single line if else statment

x = "5 is less than 2"  
if 5 < 2:
     print(x)
else:
    x = "5 is grater than 2"
    print(x)


a = [12,33,44,55,66,77,90]
search_element=34

if search_element in a:
     print("element exists")
else:
     print("elemenet does not exist")


#break statements
#after break no instruction will allow

a = [22, 33, 44, 55, 57, 89, 23]
search_nmbr = 22

for b in a:
    print(b)
    if b == search_nmbr:
        print("number found")
        break  # This will stop the loop when the number is found

print("outside loop")

#continue

c= [22, 33, 44, 55, 57, 89, 23,22]
search_nmbr = 23

for b in c:
    if b == search_nmbr:
        print("number found in list ")
        continue  # This will stop the loop when the number is found

print("outside loop")


#type casting : converting one data type in to another data type

x=22.4
b = int(x)
print(b)

"""write a program to check weather given nmbr is positive or negative"""

x = int(input("enter nmbr here: "))
if x>0:
    print("given nmbr is positive ")
elif x < 0:
     print("given nmbr is negative")
else:
    print("Given number is zero.")







    
     

