#Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
    if (n == 0 or n == 1):
        return n
    return n % 10 + sum_of_digits(n//10)

num = int(input("enter the number = "))
print("sum of digit  is " , sum_of_digits(num))
