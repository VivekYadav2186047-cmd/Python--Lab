# Leap Year Checker

# Input a year.
# Print whether it is a leap year.
year = int(input("Enter the year to check :"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("this is a leap year")

else:
    print("this is not a leap year")
