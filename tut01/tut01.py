
import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\PRIYA RAJ\OneDrive\Documents\GitHub\2001EE46_2022\tut01\octant_input.csv')
print(df)

df['Uavg'] = df['U'].mean()
df['Vavg'] = df['V'].mean()
df['Wavg'] = df['W'].mean()
df['U-Uavg'] = df['U'] - df['Uavg']
df['V-Vavg'] = df['V'] - df['Vavg']
df['W-Wavg'] = df['W'] - df['Wavg']

def find_octant(x, y, z):
    if x>0 and y>0 and z>0:
        octant = 1
    if x>0 and y>0 and z<0:
        octant = -1
    if x<0 and y>0 and z>0:
        octant = 2
    if x<0 and y>0 and z<0:
        octant = -2
    if x<0 and y<0 and z>0:
        octant = 3
    if x<0 and y<0 and z<0:
        octant = -3
    if x>0 and y<0 and z>0:
        octant = 4
    if x>0 and y<0 and z<0:
        octant = -4
    return octant

