# Data Doctor Assignment

import pandas as pd

# Creating a sample dataset
data = {
    "Name": ["Alice", "Bob", "Alice", None],
    "Age": [25, None, 25, 30],
    "City": ["New York", "los angeles", "New York", "LOS ANGELES"]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Handling missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Name"].fillna("Unknown", inplace=True)

# Removing duplicate rows
df.drop_duplicates(inplace=True)

# Standardizing text (making all text lowercase)
df["City"] = df["City"].str.lower()

print("\nCleaned Data:\n", df)