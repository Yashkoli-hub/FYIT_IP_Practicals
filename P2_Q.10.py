# Division by Zero 
try: 
    a = int(input("Enter a number: ")) 
    b = int(input("Enter another number: ")) 
    print(a / b) 
except ZeroDivisionError: 
    print("Error: Division by zero is not allowed.") 
 
# String + Number 
try: 
    s = "10" 
    n = 5 
    print(s + n) 
except TypeError: 
    print("Error: Cannot add string and integer.") 
 
# Correct way 
print(int(s) + n) 
