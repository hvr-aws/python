# find substring in a given string
s = input("Enter a string: ")
sub = input("Enter a substring to find: ")  
if sub in s:
    print(f"'{sub}' is found in '{s}'")     
else:
    print(f"'{sub}' is not found in '{s}'") 
# Output will indicate whether the substring is found or not
# Example:
# Enter a string: Hello, world!
# Enter a substring to find: world
# 'world' is found in 'Hello, world!'


