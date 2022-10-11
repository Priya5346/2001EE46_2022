#importing libraries
import pandas as pd
import numpy as np
import openpyxl as opxl
#reading file
df = pd.read_excel('C:/Users/PRIYA RAJ/OneDrive/Documents/GitHub/CS384_2022/tut03/input_octant_longest_subsequence.xlsx', 'Sheet1')

# finding the mean
df['Uavg'] = df['U'].mean()
df['Vavg'] = df['V'].mean()
df['Wavg'] = df['W'].mean()
# diffrence of original and mean value
df['U-Uavg'] = df['U'] - df['Uavg']
df['V-Vavg'] = df['V'] - df['Vavg']
df['W-Wavg'] = df['W'] - df['Wavg']

print(df)