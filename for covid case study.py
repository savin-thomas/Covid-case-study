# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 23:14:22 2025

@author: savin
"""

"""
Pseudo code

1) filter for 11th august
2) filter for 1 state, kerela
3) find death and confirmed
4) death rate = death/confirmed
5) create state list
6) create death rate list
7) loop through the state list
8) append death rate to death rate list
9) zip state list and death rate list into output variable
10) convert output to csv  
"""

import pandas as pd

data = pd.read_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/covid_19_india.csv")

# start of base code
data_11_august = data[data["Date"]=="2021-08-11"]

data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]=="Kerala"]

deaths = data_11_august_kerala["Deaths"].min()
confirmed = data_11_august_kerala["Confirmed"].min()

death_rate = deaths/confirmed

#end of base code

state_list = data["State/UnionTerritory"].unique().tolist()


death_rate_list = []
for i in state_list:
    
    data_11_august = data[data["Date"]=="2021-08-11"]

    data_11_august_kerala = data_11_august[data_11_august["State/UnionTerritory"]==i]

    deaths = data_11_august_kerala["Deaths"].min()
    confirmed = data_11_august_kerala["Confirmed"].min()

    death_rate = deaths/confirmed
    
    death_rate_list.append(death_rate)
    
output = pd.DataFrame(list(zip(state_list,death_rate_list)),columns = ["State/UnionTerritory","death_rate"])
    
output.to_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for covid data/output1.csv")
    
    