numbers = [10, 20, 30, 40, 50]
text = "Python"

print("Length of list:",  len(numbers))
print("Length of string:", len(text))
print("Sum:", sum(numbers))
print("Maximum :", max(numbers))
print("Minimum:", min(numbers))

#Manual sum
total = 0
for n in numbers:
    total += n
    print("Manual Sum:", total)
