import pandas as pd

# Sample dictionary
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 28, 30],
    'City': ['New York', 'Paris', 'London']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
