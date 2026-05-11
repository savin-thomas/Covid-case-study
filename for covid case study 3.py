# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 15:10:59 2026

@author: savin
"""

"""
Pseudo code

1) filter for 11th august
2) filter for 1 state, kerala for 11th august
3) filter for 4th august
4) filter for 1 state, kerala for 4th august
5) create death variable for 11th august, kerala
6) create death variable for 4th august, kerala
7) subtract the death variables to get the number of deaths in 1 week, this is the deaths_per_week variable
8) divide the death variable for 11th august kerala by deaths_per_week to get the number of weeks
9) multiply the number of weeeks by 7 to get the number of days, this is the doubling rate (number of days in which death count becomes double)
10) create state list
11) create doubling rate list
12) loop through each state
13) append each doubling rate to the doubling rate list 
14) zip the state list and the doubling rate list into output variable
15) convert output to csv
"""

import pandas as pd

data = pd.read_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/covid_19_india.csv")


#start of base code
data_11_august = data[data["Date"]=="2021-08-11"]
data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]=="Kerala"]

data_4_august = data[data["Date"]=="2021-08-04"]
data_4_august_kerala = data_4_august[data_4_august["State/UnionTerritory"]=="Kerala"]

deaths_11_august_kerala = data_11_august_kerala["Deaths"].min()
deaths_4_august_kerala = data_4_august_kerala["Deaths"].min()

deaths_per_week = deaths_11_august_kerala - deaths_4_august_kerala

number_of_weeks = deaths_11_august_kerala/ deaths_per_week

doubling_rate = number_of_weeks * 7

#end of base code

state_list = data["State/UnionTerritory"].unique().tolist()

doubling_rate_list = []

for i in state_list:
    
    data_11_august = data[data["Date"]=="2021-08-11"]
    data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]==i]

    data_4_august = data[data["Date"]=="2021-08-04"]
    data_4_august_kerala = data_4_august[data_4_august["State/UnionTerritory"]==i]

    deaths_11_august_kerala = data_11_august_kerala["Deaths"].min()
    deaths_4_august_kerala = data_4_august_kerala["Deaths"].min()

    deaths_per_week = deaths_11_august_kerala - deaths_4_august_kerala

    if deaths_per_week > 0:
        number_of_weeks = deaths_11_august_kerala/ deaths_per_week
        doubling_rate = number_of_weeks * 7
    else:
        doubling_rate = -999
    
    doubling_rate_list.append(doubling_rate)
    
output = pd.DataFrame(list(zip(state_list,doubling_rate_list)),columns=["State/UnionTerritory","doubling rate"])

output.to_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/output3.csv")