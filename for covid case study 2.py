# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 22:44:00 2026

@author: savin
"""

"""
Psuedo code

1) filter for 11 august
2) filter for 11 july
3) filter for 1 state, kerala for 11 august
4) filter for 1 state, kerala for 11 july
5) find death variable for 11 august
6) find death variable for 11 july
7) find confirmed variable for 11 august
8) find confirmed variable for 11 july
9) create "difference" variable for death
10 create "difference" variable for confirmed
11) find death rate: death rate = death/confirmed
12) create state list
13) create death rate list
14) loop thorugh each state
15) append death rate to death rate list
16) zip state list and death rate list into output variable
17) convert output to csv
"""

import pandas as pd

data = pd.read_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/covid_19_india.csv")

#start of base code
data_11_august = data[data["Date"]=="2021-08-11"]
data_11_july = data[data["Date"]=="2021-07-11"]

data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]=="Kerala"]
data_11_july_kerala = data_11_july[data_11_july["State/UnionTerritory"]=="Kerala"]

death_11_august_kerala = data_11_august_kerala["Deaths"].min()
death_11_july_kerala = data_11_july_kerala["Deaths"].min()

confirmed_11_august_kerala = data_11_august_kerala["Confirmed"].min()
confirmed_11_july_kerala = data_11_july_kerala["Confirmed"].min()

death_difference = death_11_august_kerala - death_11_july_kerala
confirmed_difference = confirmed_11_august_kerala - confirmed_11_july_kerala

death_rate = death_difference/confirmed_difference

#end of base code

state_list = data["State/UnionTerritory"].unique().tolist()

death_rate_list = []

for i in state_list:
    
    data_11_august = data[data["Date"]=="2021-08-11"]
    data_11_july = data[data["Date"]=="2021-07-11"]

    data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]==i]
    data_11_july_kerala = data_11_july[data_11_july["State/UnionTerritory"]==i]

    death_11_august_kerala = data_11_august_kerala["Deaths"].min()
    death_11_july_kerala = data_11_july_kerala["Deaths"].min()

    confirmed_11_august_kerala = data_11_august_kerala["Confirmed"].min()
    confirmed_11_july_kerala = data_11_july_kerala["Confirmed"].min()

    death_difference = death_11_august_kerala - death_11_july_kerala
    confirmed_difference = confirmed_11_august_kerala - confirmed_11_july_kerala

    death_rate = death_difference/confirmed_difference
    
    death_rate_list.append(death_rate)

output = pd.DataFrame(list(zip(state_list,death_rate_list)),columns=["State/UnionTerritory","death_rate"])

output.to_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/output2.csv")