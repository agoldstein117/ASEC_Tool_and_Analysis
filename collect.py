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
#%%
hh_new_names={'H_SEQ':'PH_SEQ'}
new_names={'A_MJOCC': 'Occupation','WSAL_VAL':'Salary','A_HGA':'Education','PRDTRACE':'Race','A_SEX':'Sex'}

hhpub21_new=hhpub21[['H_SEQ','GTCBSA']]
hhpub20_new=hhpub20[['H_SEQ','GTCBSA']]
hhpub19_new=hhpub19[['H_SEQ','GTCBSA']]

#CBSAFPjoining layer for geo package, PH_SEQ=P_SEQ and you will need to then add the CBSA data
pppub21=pppub21.rename(columns=new_names)
pppub20=pppub20.rename(columns=new_names)
pppub19=pppub19.rename(columns=new_names)

hhpub21_new=hhpub21_new.rename(columns=hh_new_names) 
hhpub20_new=hhpub20_new.rename(columns=hh_new_names)
hhpub19_new=hhpub19_new.rename(columns=hh_new_names)
#%%

stats_list=['PH_SEQ','Sex','Race','Occupation','Salary', 'Education']

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


concact_full_data.to_csv('final_data.csv')