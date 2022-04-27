# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:09:04 2022

@author: zev11
"""

import pandas as pd
import geopandas as gpd

pppub21=pd.read_csv('pppub21.csv',dtype=str)
pppub20=pd.read_csv('pppub20.csv',dtype=str)
pppub19=pd.read_csv('pppub19.csv',dtype=str)

hhpub21=pd.read_csv('hhpub21.csv',dtype=str)
hhpub20=pd.read_csv('hhpub20.csv',dtype=str)
hhpub19=pd.read_csv('hhpub19.csv',dtype=str)

#%%
hh_person_names={'H_SEQ':'PH_SEQ'}

hh_to_p21=hhpub21.rename(columns=hh_person_names) 
hh_to_p20=hhpub20.rename(columns=hh_person_names)
hh_to_p19=hhpub19.rename(columns=hh_person_names)


#%%
pp_hh_21merge=pppub21.merge(hh_to_p21, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_20merge=pppub20.merge(hh_to_p20, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_19merge=pppub19.merge(hh_to_p19, on='PH_SEQ', how='right', validate='m:1', indicator=True)

#%%

pp_hh_concact_list=[pp_hh_21merge,pp_hh_20merge,pp_hh_19merge]


pp_hh_data=pd.concat(pp_hh_concact_list)


#%%

pp_hh_data=pp_hh_data.drop(columns='_merge')


pp_hh_data_list=['PH_SEQ','PPPOS','GTCBSA','GESTFIPS','GEDIV','PRDTRACE','A_SEX',"A_EXPLF",'A_LFSR']

pp_hh_data=pp_hh_data[pp_hh_data_list]

pp_new_names={'GTCBSA':'CBSA','GESTFIPS':'FIPS','GEDIV':'Region','PRDTRACE':'Race','A_SEX':'Sex',"A_EXPLF":'Unempoyment_Status','A_LFSR':'In_Labor_Force'}

pp_hh_data=pp_hh_data.rename(columns=pp_new_names)

pp_hh_data=pp_hh_data.dropna()

pp_hh_data['PSID']=pp_hh_data['PH_SEQ']+pp_hh_data['PPPOS']

pp_hh_data=pp_hh_data.drop_duplicates(subset='PSID')

pp_hh_data.set_index('PSID', inplace=True)

#%%
pp_hh_data.to_csv('pp_hh_data.csv')


