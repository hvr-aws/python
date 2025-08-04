def count_vowels(word):
    return sum(char in 'aeiorAEIOU' for char in word)
word = "harha"
print("number of vowels present is:",count_vowels(word))