# Dataset Detective

import pandas as pd

# Creating a small dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, None, 22],
    "Marks": [85, 90, 78, 88, None],
    "Attendance": [90, 85, 88, 92, 87]
}

df = pd.DataFrame(data)

# Display top rows
print("Top 5 rows:\n", df.head())

# Find maximum values in numeric columns
print("\nMaximum values in each column:\n", df.max(numeric_only=True))

# Count missing values
print("\nMissing values in dataset:\n", df.isnull().sum())