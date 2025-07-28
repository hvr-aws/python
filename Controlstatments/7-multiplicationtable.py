# Multiplication Table Generator
# This program generates a multiplication table for a given number from 1 to 20.
x=int(input("Enter a number: "))
for i in range(1, 21):
    # Print the multiplication result 
    print(f"{x} x {i} = {x * i}")