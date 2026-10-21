
import string

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in string.punctuation:
        result += ch

print("String without punctuation:", result)
