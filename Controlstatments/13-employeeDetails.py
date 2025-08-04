n=int(input("enter the number of employees: "))

employee={}
for i in range (n):
    name=input("enter the employee name: ")
    salary=input("enter the employee salary: ")
    employee[name]=salary
while True:
    name=input("enter emploeyee name")
    salary=employee.get(name, -1)
    if salary == -1:
        print("employee does not exist")
    else:
        print("salary of employee is :", salary)
    choice= input("do you want to know the salary of other employees [YES/NO]")
    if choice == 'NO':
        break