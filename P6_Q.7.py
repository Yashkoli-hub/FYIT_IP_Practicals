import numpy as np

arr = np.array([10, 20, 30],
               [40, 50, 60],
               [70, 80, 90])

print("Specific Element:", arr[1, 2])

print("\nFirst Row")
print(arr[0])

print("\nSecond Coloumn")
print(arr[:1])

print("\nSlicing")
print(arr[0:2, 1:3])
