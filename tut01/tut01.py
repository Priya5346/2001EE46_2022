
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

n = len(df)

octants = []
octant_count = {1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}
for i in range(n):
    x = df.loc[i, "U-Uavg"]
    y = df.loc[i, "V-Vavg"]
    z = df.loc[i, "W-Wavg"]
    octants.append(find_octant(x, y, z))
    octant_count[find_octant(x, y, z)] = octant_count[find_octant(x, y, z)]+1
    

print(octants)
print(octant_count)