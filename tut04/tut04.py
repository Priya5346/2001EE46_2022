#importing libraries
import pandas as pd
import numpy as np
import openpyxl as opxl
#reading file
df = pd.read_excel('C:/Users/PRIYA RAJ/OneDrive/Documents/GitHub/CS384_2022/tut04/input_octant_longest_subsequence_with_range.xlsx', 'Sheet1')

# finding the mean
df['Uavg'] = df['U'].mean()
df['Vavg'] = df['V'].mean()
df['Wavg'] = df['W'].mean()
# diffrence of original and mean value
df['U-Uavg'] = df['U'] - df['Uavg']
df['V-Vavg'] = df['V'] - df['Vavg']
df['W-Wavg'] = df['W'] - df['Wavg']

# finding the octant
def identify_octant(x, y, z):
    if(x>0 and y>0 and z>0):
        octant = 1
    if(x>0 and y>0 and z<0):
        octant = -1
    if(x<0 and y>0 and z>0):
        octant = 2
    if(x<0 and y>0 and z<0):
        octant = -2
    if(x<0 and y<0 and z>0):
        octant = 3
    if(x<0 and y<0 and z<0):
        octant = -3
    if(x>0 and y<0 and z>0):
        octant = 4
    if(x>0 and y<0 and z<0):
        octant = -4
    return octant

n = len(df)


def octant_identification_count(df):
    octants = []
    octant_count = {1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}
    for i in (-1, 1, 2, -2, 3, -3, 4, -4):
        octant_count[i] = 0
    for i in range(n):
        x = df.loc[i, "U-Uavg"]
        y = df.loc[i, "V-Vavg"]
        z = df.loc[i, "W-Wavg"]
        octants.append(identify_octant(x, y, z))
        octant_count[identify_octant(x, y, z)] = octant_count[identify_octant(x, y, z)]+1
    # print(octants, '\n')
    # print(octant_count, '\n')
    return (octants, octant_count)

octants_overall = octant_identification_count(df)[0]
df['Octants'] = octants_overall
print(df)