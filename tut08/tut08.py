import openpyxl
import pandas as pd
import os

ind_inn = open("india_inns2.txt","r+") #india batting
pak_inn = open("pak_inns1.txt","r+") #pakistan batting
teams = open("teams.txt","r+")

input_team = teams.readlines()

pak_team = input_team[0]
pak_players = pak_team[23:-1:].split(",")

ind_team = input_team[2]
ind_players = ind_team[20:-1:].split(",")

print(ind_players)
print(pak_players)


lst_ind=ind_inn.readlines() #124
for i in lst_ind:
    if i=='\n':
        lst_ind.remove(i)
      

lst_pak=pak_inn.readlines() #123
for i in lst_pak:
    if i=='\n':
        lst_pak.remove(i)

print(lst_ind)
print(lst_pak)

wb = openpyxl.Workbook()
sheet = wb.active


ind_fall_of_wickets=0
pak_fall_of_wickets=0
out_pak_bat={}
out_ind_bat={}
ind_bowlers={}
pak_bowlers={}
ind_bats={}
pak_bats={}
pak_bowlers_total=0
ind_bowlers_total=0
pak_byes=0
ind_byes=0

for l in lst_pak:
    x=l.index(".")
    over_pak=l[0:x+2]
    temp=l[x+2::].split(",")
    curr_ball=temp[0].split("to") #0 2

    if f"{curr_ball[0].strip()}" not in ind_bowlers.keys() :
        ind_bowlers[f"{curr_ball[0].strip()}"]=[1,0,0,0,0,0,0]   #[over0,medan1,runs2,Wickets3, NB4, WD5, ECO6]
    elif "wide" in temp[1]:
        pass
    elif "bye" in temp[1]:
        if "FOUR" in temp[2]:
            pak_byes+=4
        elif "1" in temp[2]:
            pak_byes+=1
        elif "2" in temp[2]:
            pak_byes+=2
        elif "3" in temp[2]:
            pak_byes+=3
        elif "4" in temp[2]:
            pak_byes+=4
        elif "5" in temp[2]:
            pak_byes+=5

    else:
        ind_bowlers[f"{curr_ball[0].strip()}"][0]+=1
    
    if f"{curr_ball[1].strip()}" not in pak_bats.keys() and temp[1]!="wide":
        pak_bats[f"{curr_ball[1].strip()}"]=[0,1,0,0,0] #[runs,ball,4s,6s,sr]
    elif "wide" in temp[1] :
        pass
    else:
        pak_bats[f"{curr_ball[1].strip()}"][1]+=1
    

    if "out" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][3]+=1
        if "Bowled" in temp[1].split("!!")[0]:
            out_pak_bat[f"{curr_ball[1].strip()}"]=("b" + curr_ball[0])
        elif "Caught" in temp[1].split("!!")[0]:
            w=(temp[1].split("!!")[0]).split("by")
            out_pak_bat[f"{curr_ball[1].strip()}"]=("c" + w[1] +" b " + curr_ball[0])
        elif "Lbw" in temp[1].split("!!")[0]:
            out_pak_bat[f"{curr_ball[1].strip()}"]=("lbw  b "+curr_ball[0])

    

    if "no run" in temp[1] or "out" in temp[1] :
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=0
        pak_bats[f"{curr_ball[1].strip()}"][0]+=0
    elif "1 run" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=1
        pak_bats[f"{curr_ball[1].strip()}"][0]+=1
    elif "2 run" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=2
        pak_bats[f"{curr_ball[1].strip()}"][0]+=2
    elif "3 run" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=3
        pak_bats[f"{curr_ball[1].strip()}"][0]+=3
    elif "4 run" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=4
        pak_bats[f"{curr_ball[1].strip()}"][0]+=4
    elif "FOUR" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=4
        pak_bats[f"{curr_ball[1].strip()}"][0]+=4
        pak_bats[f"{curr_ball[1].strip()}"][2]+=1
    elif "SIX" in temp[1]:
        ind_bowlers[f"{curr_ball[0].strip()}"][2]+=6
        pak_bats[f"{curr_ball[1].strip()}"][0]+=6
        pak_bats[f"{curr_ball[1].strip()}"][3]+=1
    elif "wide" in temp[1]:
        if "wides" in temp[1]:
            # print(temp[1][1])
            ind_bowlers[f"{curr_ball[0].strip()}"][2]+=int(temp[1][1])
            ind_bowlers[f"{curr_ball[0].strip()}"][5]+=int(temp[1][1])
        else:
            ind_bowlers[f"{curr_ball[0].strip()}"][2]+=1
            ind_bowlers[f"{curr_ball[0].strip()}"][5]+=1

print(ind_bowlers)
print(pak_bats)
print(out_pak_bat)
print(pak_byes)

for l in lst_ind:
    x=l.index(".")
    over_ind=l[0:x+2]

    temp=l[x+2::].split(",")

    curr_ball=temp[0].split("to") #0 2
    if f"{curr_ball[0].strip()}" not in pak_bowlers.keys() :
        pak_bowlers[f"{curr_ball[0].strip()}"]=[1,0,0,0,0,0,0]   #[over0,medan1,runs2,Wickets3, NB4, WD5, ECO6]
    elif "wide" in temp[1]:
        pass
    elif "bye" in temp[1]:
        if "FOUR" in temp[2]:
            ind_byes+=4
        elif "1" in temp[2]:
            ind_byes+=1
        elif "2" in temp[2]:
            ind_byes+=2
        elif "3" in temp[2]:
            ind_byes+=3
        elif "4" in temp[2]:
            ind_byes+=4
        elif "5" in temp[2]:
            ind_byes+=5
    else:
        pak_bowlers[f"{curr_ball[0].strip()}"][0]+=1
    
    if f"{curr_ball[1].strip()}" not in ind_bats.keys() and temp[1]!="wide":
        ind_bats[f"{curr_ball[1].strip()}"]=[0,1,0,0,0] #[runs,ball,4s,6s,sr]
    elif "wide" in temp[1] :
        pass
    else:
        ind_bats[f"{curr_ball[1].strip()}"][1]+=1
    

    if "out" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][3]+=1
        
        if "Bowled" in temp[1].split("!!")[0]:
            out_ind_bat[f"{curr_ball[1].strip()}"]=("b" + curr_ball[0])
        elif "Caught" in temp[1].split("!!")[0]:
            w=(temp[1].split("!!")[0]).split("by")
            out_ind_bat[f"{curr_ball[1].strip()}"]=("c" + w[1] +" b " + curr_ball[0])
        elif "Lbw" in temp[1].split("!!")[0]:
            out_ind_bat[f"{curr_ball[1].strip()}"]=("lbw  b "+curr_ball[0])

    
    
    if "no run" in temp[1] or "out" in temp[1] :
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=0
        ind_bats[f"{curr_ball[1].strip()}"][0]+=0
    elif "1 run" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=1
        ind_bats[f"{curr_ball[1].strip()}"][0]+=1
    elif "2 run" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=2
        ind_bats[f"{curr_ball[1].strip()}"][0]+=2
    elif "3 run" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=3
        ind_bats[f"{curr_ball[1].strip()}"][0]+=3
    elif "4 run" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=4
        ind_bats[f"{curr_ball[1].strip()}"][0]+=4
    elif "FOUR" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=4
        ind_bats[f"{curr_ball[1].strip()}"][0]+=4
        ind_bats[f"{curr_ball[1].strip()}"][2]+=1
    elif "SIX" in temp[1]:
        pak_bowlers[f"{curr_ball[0].strip()}"][2]+=6
        ind_bats[f"{curr_ball[1].strip()}"][0]+=6
        ind_bats[f"{curr_ball[1].strip()}"][3]+=1
    elif "wide" in temp[1]:
        if "wides" in temp[1]:
            pak_bowlers[f"{curr_ball[0].strip()}"][2]+=int(temp[1][1])
            pak_bowlers[f"{curr_ball[0].strip()}"][5]+=int(temp[1][1])
        else:
            pak_bowlers[f"{curr_ball[0].strip()}"][2]+=1
            pak_bowlers[f"{curr_ball[0].strip()}"][5]+=1

print(pak_bowlers)
print(ind_bats)
print(out_ind_bat)
print(ind_byes)