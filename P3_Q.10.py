print("Menu:")
print("1. Check Even/Odd")
print("2. Find Largest")
print("3. Grade System")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    if a >= b and a >= c:
        print(f"Largest number is {a}")
    elif b >= a and b >= c:
        print(f"Largest number is {b}")
    else:
        print(f"Largest number is {c}")

elif choice == 3:
    marks = float(input("Enter marks (out of 100): "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

else:
    print("Invalid choice! Please select 1, 2, or 3.")
