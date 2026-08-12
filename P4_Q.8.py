#Input a number
num=int(input("Enter a number:"))
if num <= 1:
    print(num, "is not a Prime Number.")
else:
    isPrime = True

#Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print(num, "is a Prime Number.")
else:
    print(num, "is a not a Prime Number.")
