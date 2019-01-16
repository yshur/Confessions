import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('confessions.csv')

# See the database before doing anything
df.set_index('likes')
# print(df.shape)
# print(df.info())
# print(df.isnull().sum().sum())
print(df.describe())

# Find the correlation
print(df.corr()['likes'].sort_values())

