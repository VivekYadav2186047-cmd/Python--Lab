'''Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.'''

template = "My name is {} and i am {} years old."
name = "Johan"
age = 25

str1 = template.format(name,age)
print(str1)

print("Do the same using f-strings.")
print(f"My name is {name} and i am {age} years old")
