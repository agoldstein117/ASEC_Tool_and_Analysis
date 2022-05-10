# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:07:51 2022

@author: zev11
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)

state_um=pp_hh_data.query("Unempoyment_Status =='2'")

state_um_grouped=state_um.groupby('FIPS').size().sort_values() 

state_um=state_um_grouped.to_frame()
state_um=state_um.rename(columns={0:'Number of Unemployed'})

state_um=state_um.reset_index()

#Pandas, matplot, and seaborn, were all imported because this script will produce graphs as the end product.
#The information is also imported as a string to make it easier to manage
#The 'pp_hh_data.csv' is used for the analysis because it best demonstrates what is in the ASEC
#Since we want to find the unemployment rate for the states state_um was set to pp_hh_data.query("Unempoyment_Status =='2'")
#We then group this information by FIPS which will give use the number of unemployed individuals by state, and I used .size().sort_values() to show the number of individuals in each state
#who are unemployed. Finally I rename the column for better reference, and I make this series into a data frame to make it easier to use analysis wise.
#%%

pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)

state_em=pp_hh_data.query("Unempoyment_Status =='1'")

state_em_grouped=state_em.groupby('FIPS').size().sort_values() 

state_em=state_em_grouped.to_frame()
state_em=state_em.rename(columns={0:'Number of Employed'})

state_em=state_em.reset_index()

#I follow the same principles as above except I change the query.
#%%

unemploy_merge=state_um.merge(state_em, on='FIPS', how='right', validate='1:1', indicator=True)

unemploy_merge=unemploy_merge.drop(columns='_merge')

unemploy_merge['Total']=state_em['Number of Employed']+state_um['Number of Unemployed']
unemploy_merge['Unemployment Rate']=round((state_um['Number of Unemployed']/unemploy_merge['Total'])*100,2)

fig, ax1 = plt.subplots(dpi=300)
unemploy_merge.plot.bar(x='FIPS',y='Unemployment Rate',fontsize=7,ax=ax1, legend=False)
ax1.set_title("Unemployment Rate by State")
ax1.set_xlabel("State")
ax1.set_ylabel("Unemployment Rate")
fig.savefig('f1_state_unem.png')

#I merged the information because I want to find the total of individuals so I can later divide the number of unemployed by the total to find the unemployment rate by state.
#I accomplish this through making a new column unemploy_merge['Unemployment Rate'] and setting it equal to round((state_um['Number of Unemployed']/unemploy_merge['Total'])*100,2).
#The results are then graphed with matplot to give a visual representation of the unemployment rate by state.
#%%

occ_um=pp_hh_data.query("Unempoyment_Status =='2'")
occ_um_grouped=occ_um.groupby('Occupation_Type').size().sort_values() 
occ_um=occ_um_grouped.to_frame()
occ_um=occ_um.rename(columns={0:'Number of Unemployed'})
occ_um=occ_um.reset_index()

#I repeat the same actions I did as above for state except I do this for occupation.
#%%
occ_em=pp_hh_data.query("Unempoyment_Status =='1'")
occ_em_grouped=occ_em.groupby('Occupation_Type').size().sort_values() 
occ_em=occ_em_grouped.to_frame()
occ_em=occ_em.rename(columns={0:'Number of Employed'})

occ_em=occ_em.reset_index()

#%%

occ_unemploy_merge=occ_um.merge(occ_em, on='Occupation_Type', how='right', validate='1:1', indicator=True)

occ_unemploy_merge=occ_unemploy_merge.drop(columns='_merge')

occ_unemploy_merge['Total']=occ_em['Number of Employed']+occ_um['Number of Unemployed']
occ_unemploy_merge['Unemployment Rate']=round((occ_um['Number of Unemployed']/occ_unemploy_merge['Total'])*100,2)
#%%
fig, ax1 = plt.subplots(dpi=300)
occ_unemploy_merge.plot.bar(x='Occupation_Type',y='Unemployment Rate',fontsize=7,ax=ax1, legend=False)
ax1.set_title("Unemployment Rate by Occupation")
ax1.set_xlabel("Occupation Type")
ax1.set_ylabel("Unemployment Rate")
fig.savefig('f1_occ_unem.png')

#I graph the unemployment rate for occupation to show which occupation types had the highest levels of unemployment.

#%%

geo_um=pp_hh_data.query("Unempoyment_Status =='2'")

geo_um_grouped=geo_um.groupby(['FIPS','Occupation_Type']).size().sort_values() 

geo_um_df=geo_um_grouped.to_frame()
geo_um_df=geo_um_df.rename(columns={0:'Number of Unemployed'})

geo_um_df=geo_um_df.sort_values('FIPS')

geo_um_df=geo_um_df.reset_index()

geo_em=pp_hh_data.query("Unempoyment_Status =='1'")

geo_em_grouped=geo_em.groupby(['FIPS','Occupation_Type']).size().sort_values() 

geo_em_df=geo_em_grouped.to_frame()
geo_em_df=geo_em_df.rename(columns={0:'Number of Employed'})

geo_em_df=geo_em_df.sort_values('FIPS')

geo_em_df=geo_em_df.reset_index()

um_occ_state=geo_um_df.merge(geo_em_df,how='inner',left_on=['FIPS','Occupation_Type'], right_on=['FIPS','Occupation_Type'], indicator=True)

um_occ_state=um_occ_state.drop(columns='_merge')

um_occ_state['Total']=um_occ_state['Number of Employed']+um_occ_state['Number of Unemployed']
um_occ_state['Unemployment Rate']=round((um_occ_state['Number of Unemployed']/um_occ_state['Total'])*100,2)

um_occ_state=um_occ_state.drop(columns=['Number of Employed','Number of Unemployed','Total'])

#Now to show how the variation of unemployment by occupation changes from state to state, I start by only working with unemployed individuals.
#I then group the informaiton by both 'FIPS','Occupation_Type' but I also find the .size() and .sort_values().
#I had to sort by FIPs to better group the information by state and I had to reset the index for the analysis to work.
#I then found the number of employed individuals so I could once again find the total.
#I merged the two data sets so I could find the total and then the percent of unemployed by occupation by state that I needed. 
#I then dropped the 'Number of Employed','Number of Unemployed','Total' because they aren't needed for graphing.
#%%
um_occ_compa=um_occ_state.query("FIPS =='6' or FIPS =='48'")
um_state_dict={'6':'California','48':'Texas'}
um_occ_compa['FIPS']=um_occ_compa['FIPS'].replace(um_state_dict)

#by using a query I could then compare any states I wished to each other to determine their differences. I only used 2 because more than that would crowed the image too much.
#I used a list to show the states names as it is more visually appealing.
#%%
fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data=um_occ_compa,x='Occupation_Type',y='Unemployment Rate',hue='FIPS',ax=ax1)
ax1.set_title("Unemployment by Occupation: State Comparison")
ax1.set_xlabel("Occupation Type")
ax1.set_ylabel("Unemployment Rate")
fig.tight_layout()
fig.savefig('f1_compa.png')
#I had to use seaborn because matplot does not have the capabilities I needed for this type of comparison.
#I set x='Occupation_Type',y='Unemployment Rate', hue='FIPS' because it will show the differences between Texas and California for the occupation unemployment within each state. 
