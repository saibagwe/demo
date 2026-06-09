import pandas as pd

# Step 1: Create sample data
data = {
    "name": ["Amit", "Riya", "John", None, "Sara"],
    "age": [23, 25, None, 22, 24],
    "salary": [30000, 40000, 50000, 35000, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Fill missing values
df["name"].fillna("Unknown", inplace=True)
df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].mean(), inplace=True)

# Step 3: Remove duplicates (if any)
df.drop_duplicates(inplace=True)

# Step 4: Create new column
df["bonus"] = df["salary"] * 0.10

# Step 5: Final output
print("\nCleaned Data:")
print(df)