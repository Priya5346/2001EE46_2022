import pandas as pd
import numpy as np
import openpyxl as opxl
import scipy.stats as ss

# reading the excel file
df = pd.read_excel('C:/Users/PRIYA RAJ/OneDrive/Documents/GitHub/CS384_2022/tut05/octant_input.xlsx', 'Sheet1')

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
    return (octants, octant_count)

octants_overall = octant_identification_count(df)[0]
df['Octants'] = octants_overall

mod = 5000
no_of_ranges = int(30000/mod)
possible_octant_values = [1, -1, 2, -2, 3, -3, 4, -4]

def split_count(mod):
    df['Octant ID'] = ''
    df['Octant ID'][0] = 'Overall Count'
    df['Octant ID'][2] = '0 - ' + str(mod-1)
    for i in range (no_of_ranges-1):
        df['Octant ID'][i+3] = str((i+1)*mod) +' - '+ str((i+2)*mod-1)

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
            
            for j in possible_octant_values:
                df[str(j)][i+2] = df['Octants'][c:c+mod].value_counts()[j]
            c = c + mod



split_count(mod)
#names of octants
possible_octant_names = ['Internal outward interaction',
                    'External outward interaction',
                    'External Ejection',
                    'Internal Ejection',
                    'External inward interaction',
                    'Internal inward interaction',
                    'Internal sweep',
                    'External sweep'
                    ]
#function to find overall ranking and mod ranking
def ranking():

    overall_count = []
    mod_count = np.zeros((no_of_ranges, 8))
    mod_ranking = []
    rank1 = []
    row_num = 0
    #storing overall and mod ranking
    for i in range(8):
        overall_count.append(df[str(possible_octant_values[i])][row_num])
    row_num = row_num+2
    for i in range(no_of_ranges):
        for j in range(8):
            mod_count[i][j] = df[str(possible_octant_values[j])][row_num]
        mod_ranking.append(ss.rankdata(mod_count[i]))
        row_num = row_num + 1

    
    overall_ranking = ss.rankdata(overall_count)
    
    #initialsing columns for ranking data frame
    df['Rank 1'] = ''
    df['Rank 1'][no_of_ranges+2] = '1'
    df['Rank 2'] = ''
    df['Rank 2'][no_of_ranges+2] = '-1'
    df['Rank 3'] = ''
    df['Rank 3'][no_of_ranges+2] = '2'
    df['Rank 4'] = ''
    df['Rank 4'][no_of_ranges+2] = '-2'
    df['Rank 5'] = ''
    df['Rank 5'][no_of_ranges+2] = '3'
    df['Rank 6'] = ''
    df['Rank 6'][no_of_ranges+2] = '-3'
    df['Rank 7'] = ''
    df['Rank 7'][no_of_ranges+2] = '4'
    df['Rank 8'] = ''
    df['Rank 8'][no_of_ranges+2] = '-4'

    possible_ranks = ['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5', 'Rank 6', 'Rank 7', 'Rank 8']

    row_num = 0

    #finding octants with rank 1 for overall range
    for i in range(8):
        df[possible_ranks[i]][row_num] = 9-int(overall_ranking[i])
        if df[possible_ranks[i]][row_num]==1:
            rank1.append(i)
    row_num = row_num+2

    #finding octants with rank 1 in each  mod range
    for i in range(no_of_ranges):
        for j in range(8):
            df[possible_ranks[j]][row_num] = 9 - int(mod_ranking[i][j])
            if df[possible_ranks[j]][row_num]==1:
                rank1.append(j)
        row_num = row_num + 1
    #adding rank 1 from above into the data frame
    df['Rank 1 Octant ID'] = ''
    df['Rank 1 Octant name'] = ''

    df['Rank 1 Octant ID'][0] = possible_octant_values[rank1[0]]
    df['Rank 1 Octant name'][0] = possible_octant_names[rank1[0]]

    row_num = 2

    for i in range(no_of_ranges):
        df['Rank 1 Octant ID'][row_num] = possible_octant_values[rank1[i+1]]
        df['Rank 1 Octant name'][row_num] = possible_octant_names[rank1[i+1]]
        row_num = row_num+1

    row_num = row_num+3
    #adding rank 1 mod values into the data frame
    columns_to_use = ['1', '-1', '2']

    df[columns_to_use[0]][row_num] = 'Octant ID'
    df[columns_to_use[1]][row_num] = 'Octant Name'
    df[columns_to_use[2]][row_num] = 'Rank 1 Mod Values'
    row_num = row_num+1

    for i in range(8):
        df[columns_to_use[0]][row_num] = possible_octant_values[i]
        df[columns_to_use[1]][row_num] = possible_octant_names[i]
        df[columns_to_use[2]][row_num] = rank1[1:no_of_ranges+1].count(i)
        row_num = row_num+1



ranking()

#converting data frame into excel file
df.to_excel('my_output.xlsx')