import pandas as pd
from collections import Counter

# 1) How to check if a dataframe has any missing values?

data = {
    'Column1': [1, 2, 3, None, 5],
    'Column2': [6, None, 8, 9, 10],
    'Column3': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

has_missing_values = df.isna().any().any()

if has_missing_values:
    print("DataFrame has missing values")
else:
    print("DataFrame does not have missing values")

# 2) How to replace missing values of multiple numeric columns with the mean?

data = {
    'Column1': [1, 2, 3, None, 5],
    'Column2': [6, None, 8, 9, 10],
    'Column3': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

column_means = df.mean()

df.fillna(column_means, inplace=True)

print(df)

# 3) Given a dictionary, convert it into corresponding dataframe and display it

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 28, 30],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

print(df)

# 4) Given a dataframe, sort it by title columns

data = {
    'Title': ['C', 'A', 'B'],
    'Value': [3, 1, 2]
}
df = pd.DataFrame(data)

df_sorted = df.sort_values(by='Title')

print(df_sorted)

# 5) How to replace missing spaces in a string with the least frequent character?


def replace_spaces_with_least_frequent_char(my_str):
    char_count = Counter(my_str)

    least_frequent_char = min(char_count, key=char_count.get)

    replaced_str = my_str.replace(' ', least_frequent_char)

    return replaced_str


my_str = 'dbc deb abed ggade'
output = replace_spaces_with_least_frequent_char(my_str)
print(output)
