n = int(input("enter the number : "))
i = 1
sum = 0
for i in range(1 , n+1):
    sq = i*i
    sum = sum + sq
    i+=1
print("sum of square of first n natural number" , sum)
