import numpy as np
import pandas as ps
df = ps.read_csv('Files\\movies_metadata.csv',encoding='unicode_escape')
print(df.describe())
print(df.info())

