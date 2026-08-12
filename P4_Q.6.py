num=int(input("Enter a number:"))
original = num
reverse = 0
#Reverse the number
while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number=", reverse)
#Check palindrome
if original == reverse:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")
