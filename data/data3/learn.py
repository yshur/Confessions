import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('confessions.csv')

# See the database before doing anything
df.set_index('likes')
# print(df.shape)
# print(df.info())
# print(df.isnull().sum().sum())
# print(df.describe())

# Find the correlation
# print(df.corr()['likes'].sort_values())

# Remove outliers
# filtered_data = df[(df.college == 'Shenkar')]

# print(filtered_data.corr()['likes'].sort_values())


# Import the libraries for the machine learning
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

from sklearn import cross_validation

model = Sequential()

# Convert the value from the input (square foot) to the output (price)
# The model receives 1 input and outputs a single value
model.add(Dense(1))

# We expect the model to be sigmoid
model.add(Activation('sigmoid'))

print(model.summary())