n = int(input("Enter how many numbers: "))
total = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / n

print(f"Sum = {total}")
print(f"Average = {average:.2f}")
