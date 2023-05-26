import numpy as np
import pandas as ps
df = ps.read_csv('Files\\200wells.csv')
print(df.describe())
print(df[['porsity']].head()) 
