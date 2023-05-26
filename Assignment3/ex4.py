import pandas as pd

# Create a sample DataFrame
data = {
    'Title': ['C', 'A', 'B'],
    'Value': [3, 1, 2]
}
df = pd.DataFrame(data)

# Sort DataFrame by the "Title" column in ascending order
df_sorted = df.sort_values(by='Title')

# Display the sorted DataFrame
print(df_sorted)
