#Input list elements
n=int(input("Enter the number of elements:"))
numbers = [ ]

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)
    
#Input the element to search
search = int(input("Enter the number to search: "))

#Search the element
found = False

for i in range(len(numbers)):
    if numbers[i] == search:
      print(search, "found at position",  i)
    found = True
    break

if found == False:
    print(search, "not found in the list.")
