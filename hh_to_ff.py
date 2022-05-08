# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:11:35 2022

@author: zev11
"""

import pandas as pd


hhpub21=pd.read_csv('hhpub21.csv',dtype=str)
hhpub20=pd.read_csv('hhpub20.csv',dtype=str)
hhpub19=pd.read_csv('hhpub19.csv',dtype=str)

ffpub21=pd.read_csv('ffpub21.csv',dtype=str)
ffpub20=pd.read_csv('ffpub20.csv',dtype=str)
ffpub19=pd.read_csv('ffpub19.csv',dtype=str)
#%%

hh_family_name={'H_SEQ':'FH_SEQ'}


hh_to_f21=hhpub21.rename(columns=hh_family_name) 
hh_to_f20=hhpub20.rename(columns=hh_family_name)
hh_to_f19=hhpub19.rename(columns=hh_family_name)

#%%
ff_hh_21merge=ffpub21.merge(hh_to_f21, on='FH_SEQ', how='right', validate='m:1', indicator=True)  
ff_hh_20merge=ffpub20.merge(hh_to_f20, on='FH_SEQ', how='right', validate='m:1', indicator=True)
ff_hh_19merge=ffpub19.merge(hh_to_f19, on='FH_SEQ', how='right', validate='m:1', indicator=True)

#%%

ff_hh_concact_list=[ff_hh_21merge,ff_hh_20merge,ff_hh_19merge]

ff_hh_data=pd.concat(ff_hh_concact_list)


#%%

ff_hh_data=ff_hh_data.drop(columns='_merge')

ff_hh_data_list=['GTCBSA','GESTFIPS','GTCO','FH_SEQ','FFPOS']

ff_hh_data=ff_hh_data[ff_hh_data_list]

ff_new_names={'GTCBSA':'CBSA','GESTFIPS':'FIPS','GTCO':'County'}

ff_hh_data=ff_hh_data.rename(columns=ff_new_names)

ff_hh_data=ff_hh_data.dropna()

#%%
ff_hh_data['FHID']=ff_hh_data['FH_SEQ']+ff_hh_data['FFPOS']

ff_hh_data.set_index('FHID', inplace=True)

ff_hh_data['County']=ff_hh_data['County'].str.zfill(3)

#%%

ff_hh_data['GEOID']=ff_hh_data['FIPS']+ff_hh_data['County']

ff_hh_data=ff_hh_data.drop_duplicates(subset='FHID')
#%%
ff_hh_data.to_csv('ff_hh_data.csv')

