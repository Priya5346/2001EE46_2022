
import pandas as pd
import numpy as np
# reading file
df = pd.read_csv('C:/Users/PRIYA RAJ/OneDrive/Documents/GitHub/CS384_2022/tut01/octant_input.csv')
print(df)


# calculating mean
df['Uavg'] = df['U'].mean()
df['Vavg'] = df['V'].mean()
df['Wavg'] = df['W'].mean()
df['U-Uavg'] = df['U'] - df['Uavg']
df['V-Vavg'] = df['V'] - df['Vavg']
df['W-Wavg'] = df['W'] - df['Wavg']
print(df)

# finding octant
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


# finding octant values
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


# finding mod octant count
def split_count(mod):
    df['Octant ID'] = ''
    df['Octant ID'][0] = 'Overall Count'
    df['Octant ID'][2] = '0 - ' + str(mod-1)
    no_of_ranges = int(30000/mod)
    for i in range (no_of_ranges-1):
        df['Octant ID'][i+3] = str((i+1)*mod) +' - '+ str((i+2)*mod-1)

    possible_octant_values = [1, -1, 2, -2, 3, -3, 4, -4]

    for i in possible_octant_values:
        df[str(i)] = ''
    for i in possible_octant_values:
        df[str(i)][0] = df['Octants'].value_counts()[i]

    c = 0
    while(c<30000):
        #creating ranges using the mod value
        for i in range (no_of_ranges):
            #storing count of diff octant values
            #[c:c+mod] gives the ranges for the column 'Octant', example- 0:4999
            for j in possible_octant_values:
                df[str(j)][i+2] = df['Octants'][c:c+mod].value_counts()[j]
            c = c + mod
print(df)

# mod = int(input("Write the value of mod: "))
mod = 5000
split_count(mod)
# converting to csv file
df.to_csv("my_output.csv")
