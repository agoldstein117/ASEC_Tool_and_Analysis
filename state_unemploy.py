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


#%%

pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)

state_em=pp_hh_data.query("Unempoyment_Status =='1'")

state_em_grouped=state_em.groupby('FIPS').size().sort_values() 

state_em=state_em_grouped.to_frame()
state_em=state_em.rename(columns={0:'Number of Employed'})

state_em=state_em.reset_index()


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
#%%

occ_um=pp_hh_data.query("Unempoyment_Status =='2'")
occ_um_grouped=occ_um.groupby('Occupation_Type').size().sort_values() 
occ_um=occ_um_grouped.to_frame()
occ_um=occ_um.rename(columns={0:'Number of Unemployed'})
occ_um=occ_um.reset_index()

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
#%%
um_occ_compa=um_occ_state.query("FIPS =='6' or FIPS =='48'")
um_state_dict={'6':'California','48':'Texas'}
um_occ_compa['FIPS']=um_occ_compa['FIPS'].replace(um_state_dict)

#%%
fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data=um_occ_compa,x='Occupation_Type',y='Unemployment Rate',hue='FIPS',ax=ax1)
ax1.set_title("Unemployment by Occupation: State Comparison")
ax1.set_xlabel("Occupation Type")
ax1.set_ylabel("Unemployment Rate")
fig.tight_layout()
fig.savefig('f1_compa.png')

