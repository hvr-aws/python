"""
given total number of marks and marks scored by a student, 
calculate weather the student has passed or failed. if the percentage marks secured by the student is 
less than 40 then student needs to reappear the exam. 
"""

total_marks=int(input("enter the total marks: "))
scored_marks=int(input("enter the scored marks: "))

percentage= (scored_marks / total_marks) * 100

if(percentage<40):
        print("You need to reappear for the exam.")
else:
        print("you have passed the exam")


"""given list of students marks and total number in an exam and pass percentage as well, 
filter the students who passed and failed,"""

# Total marks and pass percentage
total_marks = 500
pass_percentage = 40

# Number of students
num_students = int(input("Enter the number of students: "))

# Iterate to get student names and marks
for _ in range(num_students):
    name = input("Enter student's name: ")
    marks = float(input(f"Enter marks for {name}: "))
    
    percentage = (marks / total_marks) * 100
    
    if percentage >= pass_percentage:
        print(f"Student: {name}, Marks: {marks} - Passed")
    else:
        print(f"Student: {name}, Marks: {marks} - Failed")
