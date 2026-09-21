import numpy as np

# Create dataset: rows = students, columns = subjects (Math, Science, English)
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
marks = np.array([
    [85, 90, 78],   # Alice
    [70, 65, 80],   # Bob
    [95, 92, 89],   # Charlie
    [60, 55, 70],   # David
    [88, 84, 91]    # Eva
])

subjects = ["Math", "Science", "English"]

print("Marks Dataset:\n", marks)

# Average marks per student (row-wise mean)
avg_per_student = np.mean(marks, axis=1)
print("\nAverage marks per student:")
for name, avg in zip(students, avg_per_student):
    print(f"  {name}: {avg:.2f}")

# Average marks per subject (column-wise mean)
avg_per_subject = np.mean(marks, axis=0)
print("\nAverage marks per subject:")
for subj, avg in zip(subjects, avg_per_subject):
    print(f"  {subj}: {avg:.2f}")

# Highest and lowest marks overall
highest_mark = np.max(marks)
lowest_mark = np.min(marks)
print(f"\nHighest mark overall: {highest_mark}")
print(f"Lowest mark overall: {lowest_mark}")

# Position of highest/lowest mark
max_pos = np.unravel_index(np.argmax(marks), marks.shape)
min_pos = np.unravel_index(np.argmin(marks), marks.shape)
print(f"Highest scored by {students[max_pos[0]]} in {subjects[max_pos[1]]}")
print(f"Lowest scored by {students[min_pos[0]]} in {subjects[min_pos[1]]}")

# Top performer (based on average)
top_student_idx = np.argmax(avg_per_student)
print(f"\nTop performer: {students[top_student_idx]} (Avg: {avg_per_student[top_student_idx]:.2f})")

# Insights
print("\n--- Insights ---")
print(f"Class average: {np.mean(marks):.2f}")
print(f"Toughest subject (lowest avg): {subjects[np.argmin(avg_per_subject)]}")
print(f"Easiest subject (highest avg): {subjects[np.argmax(avg_per_subject)]}")
print(f"Standard deviation across all marks: {np.std(marks):.2f}")
