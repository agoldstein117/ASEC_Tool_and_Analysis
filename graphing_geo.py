# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:55:36 2022

@author: zev11
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

pp_hh_data=pd.read_csv('pp_hh_data.csv',dtype=str)

geo_um=pp_hh_data.query("Unempoyment_Status =='2'")

geo_um_grouped=geo_um.groupby(['FIPS','Occupation_Type']).size().sort_values() 

geo_um_df=geo_um_grouped.to_frame()
geo_um_df=geo_um_df.rename(columns={0:'Count'})

geo_um_df=geo_um_df.sort_values('FIPS')

geo_um_df=geo_um_df.reset_index()

#%%
fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data=geo_um_df,x='FIPS',y='Count',hue='Occupation_Type',fontsize=7,ax=ax1)
ax1.set_title("Jobs Loss by Type and State")
ax1.set_xlabel("State")
ax1.set_ylabel("Number of Unemployed")
fig.savefig('f1_state_unem.png')


#%%
geo_um_df['Percentage']=round((geo_um_df['Count']/len(pp_hh_data['CBSA'])*100),2)