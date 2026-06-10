n = int(input("enter the number = "))
sum = 0
while(n>0):
    rem = n % 10
    rem = rem*rem
    sum = sum + rem
    n = n//10

print("sum of square of digits = ", sum )
