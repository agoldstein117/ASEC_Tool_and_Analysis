# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:11:23 2022

@author: zev11
"""

import pandas as pd
import geopandas as gpd

pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)
#%%
grouped_cbsa=pp_hh_data.groupby('CBSA').size().sort_values() 

print(grouped_cbsa)

grouped_fips= pp_hh_data.groupby('FIPS').size().sort_values()

print('\n',grouped_fips)

miss_CBSA=pp_hh_data['CBSA'].value_counts()['0']
total_cbsa=len(pp_hh_data['CBSA'])

prct_miss=(miss_CBSA/total_cbsa)*100

rounded=round(prct_miss,2)

print(f'\nAbout {rounded}% of the data has no cbsa codes')

#%%
grouped_race=pp_hh_data.groupby('Race').size().sort_values() 

print('\n',grouped_race)

#%%
white_pct=pp_hh_data['Race'].value_counts()['1']
total_race=len(pp_hh_data['Race'])

prct_white=(white_pct/total_race)*100

rounded_w=round(prct_white,2)
#%%
prct_nonwhite=100-rounded_w
rounded_nw=round(prct_nonwhite,2)
#%%
black_pct=pp_hh_data['Race'].value_counts()['2']
total_race=len(pp_hh_data['Race'])

prct_black=(black_pct/total_race)*100

rounded_b=round(prct_black,2)
#%%
asian_pct=pp_hh_data['Race'].value_counts()['4']
total_race=len(pp_hh_data['Race'])

prct_asian=(asian_pct/total_race)*100

rounded_a=round(prct_asian,2)

#%%

print(f'\nAbout {rounded_w}% of all of the responses are from white only individuals')
print(f'\nAbout {rounded_nw}% of all of the responses are from non white individuals')
print(f'\nAbout {rounded_b}% of the responses are from black only individuals')
print(f'\nAbout {rounded_a}% of the responses are from asian only individuals')

#%%
















