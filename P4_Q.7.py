num = int(input("Enter a number: "))

if num < 0:
    num = num * -1  # convert negative number to positive

total_digits = 0
even_digits = 0
odd_digits = 0

if num == 0:
    total_digits = 1
else:
    temp = num
    while temp > 0:
        digit = temp % 10
        total_digits += 1
        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        temp //= 10

print(f"Total digits: {total_digits}")
print(f"Even digits: {even_digits}")
print(f"Odd digits: {odd_digits}")
