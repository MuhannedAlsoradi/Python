import pandas as pd

# Create a sample DataFrame
data = {
    'Column1': [1, 2, 3, None, 5],
    'Column2': [6, None, 8, 9, 10],
    'Column3': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

# Calculate the mean of each column
column_means = df.mean()

# Replace missing values with column means
df.fillna(column_means, inplace=True)

# Output the modified DataFrame
print(df)
