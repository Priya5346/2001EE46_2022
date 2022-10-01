import pandas as pd
import numpy as np
import openpyxl as opxl
# reading the excel file
df = pd.read_excel('C:/Users/PRIYA RAJ/OneDrive/Documents/GitHub/CS384_2022/tut02/input_octant_transition_identify.xlsx', 'Sheet1')

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

mod = 5000
def split_count(mod):
    df['Octant ID'] = ''
    df['Octant ID'][0] = 'Overall Count'
    df['Octant ID'][2] = '0 - ' + str(mod-1)
    no_of_ranges = int(30000/mod)
    for i in range (no_of_ranges-1):
        df['Octant ID'][i+3] = str((i+1)*mod) +' - '+ str((i+2)*mod-1)

    possible_octant_values = [1, -1, 2, -2, 3, -3, 4, -4]

    # adding overall octant count
    for i in possible_octant_values:
        df[str(i)] = ''
    for i in possible_octant_values:
        df[str(i)][0] = df['Octants'].value_counts()[i]

    # adding mod octant count
    c = 0
    while(c<30000):
        #creating ranges using the mod value
        for i in range (no_of_ranges):
            #storing count of diff octant values
            #[c:c+mod] gives the ranges for the column 'Octant', example- 0:4999
            for j in possible_octant_values:
                df[str(j)][i+2] = df['Octants'][c:c+mod].value_counts()[j]
            c = c + mod

    # verifying the mod octant count
    df['Octant ID'][no_of_ranges+2] = 'Verified'
    
    for i in possible_octant_values:
        df[str(i)][no_of_ranges+2] = sum(df[str(i)][2:2+no_of_ranges])

    row_number = no_of_ranges+4

    df['Octant ID'][row_number] = 'Overall transition count'
    row_number = row_number+1

    for i in possible_octant_values:
        df[str(i)][row_number] = i

    df['Octant ID'][row_number] = 'count'

    # overall transition count
    octant_index = {1:0, -1:1, 2:2, -2:3, 3:4, -3:5, 4:6, -4:7}
    transition_count_matrix = np.zeros((8, 8), int)
    for i in range(n-1):
        x = octant_index[octants_overall[i]]
        y = octant_index[octants_overall[i+1]]
        transition_count_matrix[x][y] = transition_count_matrix[x][y] + 1

    row_number = row_number+1

    for i in possible_octant_values:
        for j in possible_octant_values:
            df[str(j)][row_number + octant_index[i]] = transition_count_matrix[octant_index[i]][octant_index[j]]

    for i in possible_octant_values:
        df['Octant ID'][row_number + octant_index[i]] = i

split_count(mod)
print(df)
