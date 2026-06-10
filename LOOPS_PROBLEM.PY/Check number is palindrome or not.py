n = int(input("enter the number = "))
temp = n
rev = 0

while( n > 0):
    rem = n % 10
    rev = rev*10 + rem
    n = n // 10

if (temp == rev):
    print("number is palindrome")
else:
    print("number is not palindrome")
