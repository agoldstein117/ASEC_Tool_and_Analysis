# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:13:43 2022

@author: zev11
"""
import pandas as pd
import geopandas as gpd

pppub21=pd.read_csv('pppub21.csv')
pppub20=pd.read_csv('pppub20.csv')
pppub19=pd.read_csv('pppub19.csv')

ffpub21=pd.read_csv('ffpub21.csv')
ffpub20=pd.read_csv('ffpub20.csv')
ffpub19=pd.read_csv('ffpub19.csv')
#%%
ff_person_names={'FH_SEQ':'PH_SEQ'}

ff_to_p21=ffpub21.rename(columns=ff_person_names)
ff_to_p20=ffpub20.rename(columns=ff_person_names)
ff_to_p19=ffpub19.rename(columns=ff_person_names)


#%%
pp_ff_21merge=pppub21.merge(ff_to_p21, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_20merge=pppub20.merge(ff_to_p20, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_19merge=pppub19.merge(ff_to_p19, on='PH_SEQ', how='left', validate='m:m', indicator=True)


#%%

pp_ff_concact_list=[pp_ff_21merge,pp_ff_20merge,pp_ff_19merge]

pp_ff_data=pd.concat(pp_ff_concact_list)

#%%

pp_ff_data=pp_ff_data.drop(columns='_merge')

pp_ff_data=pp_ff_data.dropna()
#%%

pp_ff_data.to_csv('pp_ff_data.csv')

#%%

dups=pp_hh_data.duplicated(subset='PH_SEQ', keep=False)
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


