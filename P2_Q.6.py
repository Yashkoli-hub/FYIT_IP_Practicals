import math

length = float(input("Enter Rectangle length"))
breadth = float(input("Enter Rectangle breadth"))

area_rect = length * breadth
perimeter_rect = 2 * (length + breadth)

radius = float(input("Enter Circle Radius"))

area_circle = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("\nRectangle")
print("Area =",area_rect)
print("Perimeter=", perimeter_rect)

print("\nCircle")
print("Area =", round(area_circle, 2))
print("Circumference =", round(circumference,2))
    

