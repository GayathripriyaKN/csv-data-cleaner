
import pandas as pd

# Read the CSV file
df = pd.read_csv("sample data/sample.csv")

print("Original Data:")
print(df)

# Display missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numeric values with the median
for column in df.columns:
    if df[column].isnull().any():
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())
        else:
            df[column] = df[column].fillna("Unknown")

# Display cleaned data
print("\nCleaned Data:")
print(df)

# Print a small summary
print("\nDataset Summary:")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nNumeric Summary:")
print(df.describe())

# Save cleaned data
df.to_csv("cleaned_sample.csv", index=False)
print("\nCleaned data saved to cleaned_sample.csv")
