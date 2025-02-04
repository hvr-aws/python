""" Match statements"""

user = int(input("enter the number: "))
match user:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
print("completed")

user = int(input("enter the number: "))
match user:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("something")
print("completed")

"""Nested for loop"""

list_2d = [[1,2,3],[11,22,33],[4,5,6]]
for ele in list_2d:
    print(ele)

for ele_1 in ele:
    print(ele_1)
