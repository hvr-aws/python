s = int(input("Enter the number of rows for the right-angled triangle: "))
for i in range(1, s + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Move to the next line after each row
# This code prints a right-angled triangle pattern using asterisks.
# The outer loop iterates through the number of rows,
# and the inner loop prints the asterisks for each row. 
# The `end=""` in the print function prevents a newline after printing each asterisk.
# The `print()` at the end of the inner loop moves to the next line after each row is printed.
# Example input: 5
# Example output for input 5:
# *
# **
# ***
# ****
# *****
# This code prints a right-angled triangle pattern using asterisks.
