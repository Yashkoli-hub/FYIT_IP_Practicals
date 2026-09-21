student ={
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    }
print("Sorted by keys:")
for key in sorted(student):
 print(key, student[key])
for key, value in sorted (student.items(), key=lambda x:x[1]):
 print(key, value)
