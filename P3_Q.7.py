num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter thired number:"))
operator = input("Enter operator (+, - , *, /):")

if operator =="+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 !=0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
        print("Invaild operator! Please enter +, -, *, or /.")
