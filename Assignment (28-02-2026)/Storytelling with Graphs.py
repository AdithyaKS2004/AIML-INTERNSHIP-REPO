# Storytelling with Graphs

import matplotlib.pyplot as plt

# Sample data
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 90, 78, 80, 95]

# Bar Chart
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()

# Histogram
plt.hist(marks)
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()