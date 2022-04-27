# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:53:48 2022

@author: zev11
"""

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
hh_person_names={'H_SEQ':'PH_SEQ'}
hh_family_name={'H_SEQ':'FH_SEQ'}
ff_person_names={'FH_SEQ':'PH_SEQ'}



hh_to_p21=hhpub21.rename(columns=hh_person_names) 
hh_to_p20=hhpub20.rename(columns=hh_person_names)
hh_to_p19=hhpub19.rename(columns=hh_person_names)

hh_to_f21=hhpub21.rename(columns=hh_family_name) 
hh_to_f20=hhpub20.rename(columns=hh_family_name)
hh_to_f19=hhpub19.rename(columns=hh_family_name)

ff_to_p21=ffpub21.rename(columns=ff_person_names)
ff_to_p20=ffpub20.rename(columns=ff_person_names)
ff_to_p19=ffpub19.rename(columns=ff_person_names)

#%%
pp_hh_21merge=pppub21.merge(hh_to_p21, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_20merge=pppub20.merge(hh_to_p20, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_19merge=pppub19.merge(hh_to_p19, on='PH_SEQ', how='right', validate='m:1', indicator=True)

#%%
ff_hh_21merge=ffpub21.merge(hh_to_f21, on='FH_SEQ', how='right', validate='m:1', indicator=True)  
ff_hh_20merge=ffpub20.merge(hh_to_f20, on='FH_SEQ', how='right', validate='m:1', indicator=True)
ff_hh_19merge=ffpub19.merge(hh_to_f19, on='FH_SEQ', how='right', validate='m:1', indicator=True)


#%%
pp_ff_21merge=pppub21.merge(ff_to_p21, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_20merge=pppub20.merge(ff_to_p20, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_19merge=pppub19.merge(ff_to_p19, on='PH_SEQ', how='left', validate='m:m', indicator=True)

#%%
pppub21_m1=pppub21.merge(hhpub21, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pppub20_m1=pppub20.merge(hhpub20, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pppub19_m1=pppub19.merge(hhpub19, on='PH_SEQ', how='right', validate='m:1', indicator=True)

#%%
pppub21_m2=pppub21_m1.merge(ffpub21, on='PH_SEQ', how='right', validate='1:m', indicator=True)
pppub20_m2=pppub20_m1.merge(ffpub20, on='PH_SEQ', how='right', validate='1:m', indicator=True)
pppub19_m2=pppub19_m1.merge(ffpub19, on='PH_SEQ', how='right', validate='1:m', indicator=True)


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




