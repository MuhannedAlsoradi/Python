import pandas as pd

# Create a sample DataFrame
data = {
    'Column1': [1, 2, 3, None, 5],
    'Column2': [6, None, 8, 9, 10],
    'Column3': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

# Check if DataFrame has any missing values
has_missing_values = df.isna().any().any()

# Output the result
if has_missing_values:
    print("DataFrame has missing values")
else:
    print("DataFrame does not have missing values")
