# String Slicing and Indexing
# Given text = "Python Programming", do the following:

# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
print("Print the first 6 characters")
text = "Python Programming"
print(text[0:6])


print("the last 6 character")
print(text[-6:])
print(len(text))

print("Print every second character from the string")
#print(text[0:18:2])
print(text[::2])

print("Reverse the string text using slicing.")
print(text[::-1])
