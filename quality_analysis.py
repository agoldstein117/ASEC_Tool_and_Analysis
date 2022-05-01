# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:11:23 2022

@author: zev11
"""

import pandas as pd
import matplotlib.pyplot as plt


pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)

#%%
grouped_cbsa=pp_hh_data.groupby('CBSA').size().sort_values() 

miss_CBSA=pp_hh_data['CBSA'].value_counts()['0']
total_cbsa=len(pp_hh_data['CBSA'])

prct_miss=(miss_CBSA/total_cbsa)*100

rounded_cbsa=round(prct_miss,2)

print('GEOGRAPHIC INFORMATION:')
print('\nCBSA Code Information:')
print(f'About {rounded_cbsa}% of the data has no cbsa codes')

cbsa_df=grouped_cbsa.to_frame()
cbsa_df=cbsa_df.rename(columns={0:'Count'})
cbsa_df['Percentage']=round((cbsa_df['Count']/len(pp_hh_data['CBSA'])*100),2)
#%%
grouped_fips= pp_hh_data.groupby('FIPS').size().sort_values()

most_fips_pct=pp_hh_data['FIPS'].value_counts()['6']
total_fips=len(pp_hh_data['FIPS'])

prct_top=(most_fips_pct/total_fips)*100

rounded_top=round(prct_top,2)

sec_most_fips_pct=pp_hh_data['FIPS'].value_counts()['48']

prct_sec=(sec_most_fips_pct/total_fips)*100

rounded_sec=round(prct_sec,2)

third_most_fips_pct=pp_hh_data['FIPS'].value_counts()['12']

prct_third=(third_most_fips_pct/total_fips)*100

rounded_third=round(prct_third,2)

print('\nFIPS Code Information:')
print(f'About {rounded_top}% of the entries have a Californian FIPS code')
print(f'\nAbout {rounded_sec}% of the entries have a Texan FIPS code')
print(f'\nAbout {rounded_third}% of the entries have a Floridian FIPS code')

fips_df=grouped_fips.to_frame()
fips_df=fips_df.rename(columns={0:'Count'})
fips_df['Percentage']=round((fips_df['Count']/len(pp_hh_data['FIPS'])*100),2)
#%%
grouped_county= pp_hh_data.groupby('County').size().sort_values()

missing_county_pct=pp_hh_data['County'].value_counts()['0']
total_county=len(pp_hh_data['County'])

prct_top_county=(missing_county_pct/total_county)*100

rounded_top_county=round(prct_top_county,2)

print('\nCounty Code Information:')
print(f'About {rounded_top_county}% of the entries have no county code information')

county_df=grouped_county.to_frame()
county_df=county_df.rename(columns={0:'Count'})
county_df['Percentage']=round((county_df['Count']/len(pp_hh_data['County'])*100),2)

#%%
grouped_region= pp_hh_data.groupby('Region').size().sort_values()

most_region_pct=pp_hh_data['Region'].value_counts()['5']
total_region=len(pp_hh_data['Region'])

prct_most_region=(most_region_pct/total_region)*100

rounded_most_reg=round(prct_most_region,2)

sec_most_region_pct=pp_hh_data['Region'].value_counts()['9']

prct_sec_reg=(sec_most_region_pct/total_region)*100

rounded_sec_reg=round(prct_sec_reg,2)

third_most_region_pct=pp_hh_data['Region'].value_counts()['8']

prct_third_reg=(third_most_region_pct/total_region)*100

rounded_third_reg=round(prct_third_reg,2)

print('\nRegion Information:')
print(f'About {rounded_most_reg}% of the entries are located in the South Atlantic Region')
print(f'\nAbout {rounded_sec_reg}% of the entries of the entries are located in the Pacific Region')
print(f'\nAbout {rounded_third_reg}% of the entries of the entries are located in the Mountain Region')

region_df=grouped_region.to_frame()
region_df=region_df.rename(columns={0:'Count'})
region_df['Percentage']=round((region_df['Count']/len(pp_hh_data['Region'])*100),2)
#%%
grouped_race=pp_hh_data.groupby('Race').size().sort_values() 

white_pct=pp_hh_data['Race'].value_counts()['1']
total_race=len(pp_hh_data['Race'])
prct_white=(white_pct/total_race)*100

rounded_w=round(prct_white,2)
prct_nonwhite=100-rounded_w
rounded_nw=round(prct_nonwhite,2)

black_pct=pp_hh_data['Race'].value_counts()['2']
prct_black=(black_pct/total_race)*100
rounded_b=round(prct_black,2)

asian_pct=pp_hh_data['Race'].value_counts()['4']
prct_asian=(asian_pct/total_race)*100
rounded_a=round(prct_asian,2)

#%%
race_df=grouped_race.to_frame()
race_df=race_df.rename(columns={0:'Count'})
race_df['Percentage']=round((race_df['Count']/len(pp_hh_data['Race'])*100),2)

print('\nDEMOGRAPHIC INFORMATION:')
print('\n',race_df['Percentage'])
print('\nRacial Information:')
print(f'About {rounded_w}% of all of the responses are from white only individuals')
print(f'\nAbout {rounded_nw}% of all of the responses are from non white individuals')
print(f'\nAbout {rounded_b}% of the responses are from black only individuals')
print(f'\nAbout {rounded_a}% of the responses are from asian only individuals')

#%%

grouped_unemployment=pp_hh_data.groupby('Unempoyment_Status').size().sort_values() 

na_employ=pp_hh_data['Unempoyment_Status'].value_counts()['0']
total_employ=len(pp_hh_data['Unempoyment_Status'])
prct_naemply=(na_employ/total_employ)*100
rounded_naemply=round(prct_naemply,2)
prct_naemply_info=100-rounded_naemply
rounded_emply_info=round(prct_naemply_info,2)

employed=pp_hh_data['Unempoyment_Status'].value_counts()['1']
prct_employed=(employed/total_employ)*100
rounded_emplyoyed=round(prct_employed,2)

unemployed=pp_hh_data['Unempoyment_Status'].value_counts()['2']
prct_unemployed=(unemployed/total_employ)*100
rounded_unemplyoyed=round(prct_unemployed,2)

employment_total= employed+unemployed
unemployment_rate=round((unemployed/employment_total)*100,2)

employ_df=grouped_unemployment.to_frame()
employ_df=employ_df.rename(columns={0:'Count'})
employ_df['Percentage']=round((employ_df['Count']/len(pp_hh_data['Unempoyment_Status'])*100),2)


print('\nEMPLOYMENT RELATED INFORMATION:')
print('\n',employ_df['Percentage'])
print(f'\nAbout {rounded_emply_info}% of all of the responses have employment status information')
print(f'\nAbout {rounded_emplyoyed}% of all of the responses are employed individuals')
print(f'\nAbout {rounded_unemplyoyed}% of all of the responses are unemployed individuals')
print(f'\nThe unemployment rate according to the data is {unemployment_rate}%')

#%%
grouped_occupation=pp_hh_data.groupby('Occupation_Type').size().sort_values() 


occupation_df=grouped_occupation.to_frame()
occupation_df=occupation_df.rename(columns={0:'Count'})
occupation_df['Percentage']=round((occupation_df['Count']/len(pp_hh_data['Occupation_Type'])*100),2)

print('\nPercentage Representation by Occupation :')
print('\n',occupation_df['Percentage'])

#%%
fig1, ax1 = plt.subplots(dpi=300)
fips_df.plot.bar(y='Percentage',fontsize=7,ax=ax1)
ax1.set_xlabel('FIPS Codes')
ax1.set_ylabel('Percent of Responses')
ax1.set_title('Where Are the Responses Coming From?(FIPS Codes)')
fig1.tight_layout()
fig1.savefig('fips_figure.png')
#%%
fig1, ax1 = plt.subplots(dpi=300)
county_df.plot.bar(y='Percentage',fontsize=4,ax=ax1)
ax1.set_xlabel('County Codes')
ax1.set_ylabel('Percent of Responses')
ax1.set_title('What is Missing)')
fig1.tight_layout()
fig1.savefig('county_figure.png')
#%%
fig1, ax1 = plt.subplots(dpi=300)
employ_df.plot.bar(y='Percentage',fontsize=10 ,ax=ax1)
ax1.set_xlabel('Employment Status')
ax1.set_ylabel('Percent of Responses')
ax1.set_title('Employment')
fig1.tight_layout()
fig1.savefig('Employ_figure.png')
#%%
fig1, ax1 = plt.subplots(dpi=300)
occupation_df.plot.bar(y='Percentage',ax=ax1)
ax1.set_xlabel('Occupation type')
ax1.set_ylabel('Percent of Responses')
ax1.set_title('Employment by Type')
fig1.tight_layout()
fig1.savefig('occupation_figure.png')

#%%
fig1, ax1 = plt.subplots(dpi=300)
race_df.plot.bar(y='Percentage',fontsize=7,ax=ax1)
ax1.set_xlabel('Race')
ax1.set_ylabel('Percent of Responses')
ax1.set_title('Racial Make Up of Responses')
fig1.tight_layout()
fig1.savefig('race_figure.png')



