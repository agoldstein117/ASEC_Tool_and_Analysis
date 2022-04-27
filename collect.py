# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:23:04 2022

@author: zev11
"""
import pandas as pd
import geopandas as gpd

pppub21=pd.read_csv('pppub21.csv')
pppub20=pd.read_csv('pppub20.csv')
pppub19=pd.read_csv('pppub19.csv')

hhpub21=pd.read_csv('hhpub21.csv')
hhpub20=pd.read_csv('hhpub20.csv')
hhpub19=pd.read_csv('hhpub19.csv')

ffpub21=pd.read_csv('ffpub21.csv')
ffpub20=pd.read_csv('ffpub20.csv')
ffpub19=pd.read_csv('ffpub19.csv')
#%%
hhpub21_new=hhpub21[['H_SEQ','GTCBSA']]
hhpub20_new=hhpub20[['H_SEQ','GTCBSA']]
hhpub19_new=hhpub19[['H_SEQ','GTCBSA']]

ffpub21_new=ffpub21[['FH_SEQ','FFPOS','FTOT_R']]
ffpub20_new=ffpub21[['FH_SEQ','FFPOS','FTOT_R']]
ffpub19_new=ffpub21[['FH_SEQ','FFPOS','FTOT_R']]

pp_new_names={"A_EXPLF":'Unempoyment_Status','A_LFSR':'In_Labor_Force','UC_YN': 'Received_UIB','UC_VAL':'UIB_Amount','A_WKSLK':'Duration of unemployment','NXTRES':'Moving_Status','PRDTRACE':'Race','A_SEX':'Sex'}
hh_new_names={'H_SEQ':'PH_SEQ'}
ff_new_names={'F_SEQ':'PH_SEQ'}

#CBSAFPjoining layer for geo package, PH_SEQ=P_SEQ and you will need to then add the CBSA data
pppub21=pppub21.rename(columns=pp_new_names)
pppub20=pppub20.rename(columns=pp_new_names)
pppub19=pppub19.rename(columns=pp_new_names)

hhpub21_new=hhpub21_new.rename(columns=hh_new_names) 
hhpub20_new=hhpub20_new.rename(columns=hh_new_names)
hhpub19_new=hhpub19_new.rename(columns=hh_new_names)


#%%

stats_list=['PH_SEQ','In Labor Force?','Unempoyment Status','Received UIB','UIB Amount','Duration of unemployment','Moving Status', 'Race','Sex']

pppub21=pppub21[stats_list]
pppub20=pppub20[stats_list]
pppub19=pppub19[stats_list]

pppub21['Year']=2021
pppub20['Year']=2020
pppub19['Year']=2019

pppub21_merged=pppub21.merge(hhpub21_new, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pppub20_merged=pppub20.merge(hhpub20_new, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pppub19_merged=pppub19.merge(hhpub19_new, on='PH_SEQ', how='right', validate='m:1', indicator=True)


#%%

pppub_concact_list=[pppub21_merged,pppub20_merged,pppub19_merged]

concact_full_data=pd.concat(pppub_concact_list)

concact_full_data=concact_full_data.drop(columns='_merge')

concact_full_data=concact_full_data.dropna()

concact_full_data.to_csv('concact_full_data.csv')
#%%
unemployment= concact_full_data['Unempoyment Status']

cbsa= concact_full_data['GTCBSA']

status_trimmed=concact_full_data.where(unemployment>1,)

status_trimmed=status_trimmed.dropna()

new_trimmed=status_trimmed.copy() 

status=new_trimmed['Unempoyment Status']

new_trimmed=new_trimmed.where(status>0,)

dups=new_trimmed.duplicated(subset='PH_SEQ', keep=False)
#%%
final_data=new_trimmed.drop_duplicates(subset='PH_SEQ')

grouped=final_data.groupby('GTCBSA').size().sort_values() 

print(grouped) 


#%%

moving_grouped=final_data.groupby('Moving Status').size().sort_values()

print(moving_grouped) 


print('\n',new_trimmed['Received UIB'].value_counts()) 

final_data.to_csv('final_data.csv')
#%%

avg_ui_list=['Received UIB','UIB Amount','GTCBSA']
avg_ui=final_data[avg_ui_list]
r_ui=avg_ui['Received UIB']
avg_ui=avg_ui.where(r_ui<2,)
avg_ui=avg_ui.dropna()
avg_ui_amount=avg_ui.drop(columns='Received UIB')
avg_ui_group=avg_ui_amount.groupby('GTCBSA').sum()
#%%
numbr_avg_ui_group=avg_ui_amount.groupby('GTCBSA').count()

avg_amount_ui=avg_ui_group/numbr_avg_ui_group 

rounded_amounts=round(avg_amount_ui,)

print('\n',rounded_amounts) 




