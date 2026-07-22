num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)
             
