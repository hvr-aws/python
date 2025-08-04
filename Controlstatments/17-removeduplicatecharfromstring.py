s = input("Enter a string: ")
# remove duplicate characters from a string
result = [] 
for char in s:
    if char not in result:
        result.append(char) 
print(" ".join(result))  # Join the list into a string and print it

