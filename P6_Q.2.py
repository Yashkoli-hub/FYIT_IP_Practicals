matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print("Row-wise Traversal")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

print("\nColoumn-wise Traversal")
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        print(matrix[j] [i], end=" ")
    print()
