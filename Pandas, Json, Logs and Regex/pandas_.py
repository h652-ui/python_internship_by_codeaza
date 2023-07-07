import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({"a" : [4, 5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]}, index = [1, 2, 3])
print(df)
print()

df = pd.DataFrame([[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])
print(df)
print()

df = pd.DataFrame({"a" : [4 ,5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]}, index = pd.MultiIndex.from_tuples([('d', 1), ('d', 2), ('e', 2)], names=['n', 'v']))

grouped = df.groupby('v')
for name, group in grouped:
    print("Group:", name)
    print(group)
    print()

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Age': [25, 31, 29, 35, 28],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}

df = pd.DataFrame(data)

# Method chaining example
result = (
    df[df['Gender'] == 'Male']  # Filter rows where Gender is Male
    .sort_values('Age')  # Sort by Age column
    .reset_index(drop=True)  # Reset index
    .loc[:, ['Name', 'Age']]  # Select only Name and Age columns
    .rename(columns={'Name': 'First Name'})  # Rename the Name column
    .head(3)  # Select the first 3 rows
)

print(result)

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Alice'],
    'Age': [25, 31, 29, 35, 28, 25],
    'Length': [8, 9, 6, 10, 7, 8],
    'Value': [100, 200, 150, 250, 180, 100]
}

df = pd.DataFrame(data)

# Extract rows that meet logical criteria
filtered_df = df[df['Length'] > 7]
print("Filtered DataFrame:")
print(filtered_df)
print()

# Remove duplicate rows (only considers columns)
deduplicated_df = df.drop_duplicates()
print("Deduplicated DataFrame:")
print(deduplicated_df)
print()

# Randomly select a fraction of rows
fraction_sample = df.sample(frac=0.5)
print("Fraction Sampled DataFrame:")
print(fraction_sample)
print()

# Randomly select a specific number of rows
n_sample = df.sample(n=3)
print("Random Sampled DataFrame (n=3):")
print(n_sample)
print()

# Select and order top n entries
top_entries = df.nlargest(3, 'Value')
print("Top 3 Entries based on 'Value':")
print(top_entries)
print()

# Select and order bottom n entries
bottom_entries = df.nsmallest(2, 'Age')
print("Bottom 2 Entries based on 'Age':")
print(bottom_entries)
print()

# Select first n rows
first_n_rows = df.head(3)
print("First 3 Rows:")
print(first_n_rows)
print()

# Select last n rows
last_n_rows = df.tail(2)
print("Last 2 Rows:")
print(last_n_rows)

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Length': [8, 9, 6, 10, 7],
    'Width': [7, 6, 8, 5, 9]
}

df = pd.DataFrame(data)

# Filtering rows using query()
filtered_df = df.query('Length > 7')
print("Rows where Length > 7:")
print(filtered_df)
print()

filtered_df = df.query('Length > 7 and Width < 8')
print("Rows where Length > 7 and Width < 8:")
print(filtered_df)
print()

filtered_df = df.query('Name.str.startswith("A")', engine="python")
print("Rows where Name starts with 'A' (using Python engine):")
print(filtered_df)

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
}

df = pd.DataFrame(data)

# Sum values of each object
print("Sum:")
print(df.sum())
print()

# Count non-NA/null values of each object
print("Count:")
print(df.count())
print()

# Median value of each object
print("Median:")
print(df.median())
print()

# Quantiles of each object
print("Quantiles:")
print(df.quantile([0.25, 0.75]))
print()

# Apply function to each object
print("Apply (Square root):")
print(df.apply(lambda x: x**0.5))
print()

# Minimum value in each object
print("Minimum:")
print(df.min())
print()

# Maximum value in each object
print("Maximum:")
print(df.max())
print()

# Mean value of each object
print("Mean:")
print(df.mean())
print()

# Variance of each object
print("Variance:")
print(df.var())
print()

# Standard deviation of each object
print("Standard Deviation:")
print(df.std())

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, np.nan, 15]
}

df = pd.DataFrame(data)

# Drop rows with any column having NA/null data
dropped_df = df.dropna()
print("DataFrame after dropping rows with NA values:")
print(dropped_df)
print()

# Replace all NA/null data with a specific value
filled_df = df.fillna(0)
print("DataFrame after filling NA values with 0:")
print(filled_df)


# Create a sample DataFrame
data = {
    'Length': [5, 8, 10, 4, 6],
    'Height': [3, 6, 2, 7, 5],
    'Depth': [2, 4, 3, 1, 2]
}

df = pd.DataFrame(data)

# Compute and append a new column using assign()
df = df.assign(Area=lambda df: df.Length * df.Height)
print("DataFrame with 'Area' column:")
print(df)
print()

# Add a single column using assignment
df['Volume'] = df.Length * df.Height * df.Depth
print("DataFrame with 'Volume' column:")
print(df)
print()

# Bin a column into n buckets using pd.qcut()
df['Length_Buckets'] = pd.qcut(df['Length'], 3, labels=False)
print("DataFrame with 'Length_Buckets' column:")
print(df)
# Create a sample DataFrame
data = {
    'w': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'h': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    'd': [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
}

df = pd.DataFrame(data)

# Create a histogram for each column
df.plot.hist()
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Create a scatter chart using pairs of points
df.plot.scatter(x='w', y='h')
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Scatter Plot')
plt.show()
