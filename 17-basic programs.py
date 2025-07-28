# 17-input read and display student details

studentid=int(input("enter student id"))
name = input("enter student name")
marks=float(input("enter marks scored"))
print("Id:",studentid, "name:",name, "marks:",marks)


# average of students

a,b,c= [int(x) for x in input("enter three intiger numbers").split()]
average=(a+b+c)/3
print("average of three numbers is :",average)


# area of circle
import math
r=float(input("enter the radius of circle:" ))
area=math.pi*r**2
print("area of circle is:", area)