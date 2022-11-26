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

# batting [runs,ball,4s,6s,sr]
# bowling [over,medan,runs,Wickets, NB, WD, ECO]
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

