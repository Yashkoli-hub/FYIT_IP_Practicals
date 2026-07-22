age = int(input("Enter your age: "))
nationality = input("Enter your nationaliity: ")

if  age >= 18:
    if nationality.lower() == "indian":
        print("Eligible to Vote.")
    else:
        print("Not Eligible to Vote (Only Indian citizens can vote).")
else:
    print("Not Eligible to Vote (Age must be 18 or above).")
