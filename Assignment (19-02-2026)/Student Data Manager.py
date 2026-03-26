# Student Data Manager Program
# This program stores marks of 5 students,
# finds the topper, calculates class average,
# and assigns grades based on marks.

students = {
    "Rahul": 85,
    "Sneha": 92,
    "Amit": 76,
    "Priya": 88,
    "Karan": 67
}

# Finding topper
topper = max(students, key=students.get)
print("Topper of the class:", topper, "-", students[topper], "marks")

# Calculating class average
average = sum(students.values()) / len(students)
print("Class Average:", average)

# Assigning grades
print("\nStudent Grades:")

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"
    
    print(name, ":", marks, "Grade", grade)