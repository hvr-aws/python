# reverse the characters in the words in runtime
# Example: "Hello World" should become "olleH dlroW"    

s = input("Enter a sentence: ")
temp = s.split()
print(temp)
result = []
i = 0
# Using a while loop to reverse each word

while i < len(temp):
    result.append(temp[i][::-1])    
    i += 1
print(" ".join(result))
    