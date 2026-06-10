#Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

def calculate_area(length , width = 10):
    area = length * width
    return area 
print(f"the area of the rectangle is{calculate_area(5,6)} ")

print(calculate_area(5))
