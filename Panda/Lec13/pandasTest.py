import pandas as ps
import numpy as np

df = ps.read_csv('Files\\movies_metadata.csv', encoding='unicode_escape')
print(df.head())
print(df.describe())
print(df.info())
print(df[['budget']].head())
print(df[['budget', 'adult']].head())
print(df.loc[1:2, ['budget', 'adult']])
print(df.iloc[1:2, [1, 3]])
print(df['budget'].values)
arr = df['budget'].values
df.rename(columns={'budget': 'newBudget'}, inplace=True)
print(df[['newBudget']].head())
df['zeros'] = np.zeros(len(df))
print(df.head())
df.drop('zeros', axis=1, inplace=True)
print(df.head())
print(df.drop(1).head())
print(df.head())
print(df.sort_values('newBudget', inplace=True, ascending=True))
print(df.head())
df.reset_index(inplace=True, drop=True)
print(df.head())
df[r'% budget'] = df['newBudget']*100
print(df.head())
df['budgetType'] = np.where(df['newBudget'] > 1000, 'high', 'low')
print(df.head())
print(df[df['budgetType'] == 'high'].head())
df.at[1, 'budgetType'] = None
print(df.head())
print(df[df['budgetType'].isnull()])
df.dropna(inplace=True)
print(df.head())
df_new = ps.DataFrame(
    {'new_title': ['A', 'B', 'C', 'D', 'E'], 'new_id': [1, 2, 3, 4, 5]})
print(df_new.head())
df_new.sort_values('new_title', ascending=False,
                   ignore_index=True, inplace=True)
print(df_new.head())
df1 = df.iloc[0:3, 2:]
print(df1.head())
df2 = df.iloc[10:13, 2:]
print(df2.head())
df3 = ps.concat([df1, df2], axis=0)
print(df3.head())
df.to_csv('Files\\new_csv.csv',index=False)