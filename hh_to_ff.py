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

#I imported pandas here because this tool works with data frames
#these are the household and familiy CSVs from the ASEC we will be using this to get the information we want to work with.
#%%

hh_family_name={'H_SEQ':'FH_SEQ'}

hh_to_f21=hhpub21.rename(columns=hh_family_name) 
hh_to_f20=hhpub20.rename(columns=hh_family_name)
hh_to_f19=hhpub19.rename(columns=hh_family_name)

#I created the dictionary and renamed the columns in hhpub so we can merge the family and household CSVs
#%%
ff_hh_21merge=ffpub21.merge(hh_to_f21, on='FH_SEQ', how='right', validate='m:1', indicator=True)  
ff_hh_20merge=ffpub20.merge(hh_to_f20, on='FH_SEQ', how='right', validate='m:1', indicator=True)
ff_hh_19merge=ffpub19.merge(hh_to_f19, on='FH_SEQ', how='right', validate='m:1', indicator=True)

#I merged the data on FH_SEQ because that is the connector the ASEC uses to match household and family information
#%%

ff_hh_concact_list=[ff_hh_21merge,ff_hh_20merge,ff_hh_19merge]

ff_hh_data=pd.concat(ff_hh_concact_list)

#I made the list ff_hh_concact_list so I can concatenate the information from 2019-2021, and then dropped the merge indicator since we don't need it.
#%%

ff_hh_data=ff_hh_data.drop(columns='_merge')

ff_hh_data_list=['GTCBSA','GESTFIPS','GTCO','FH_SEQ','FFPOS']

ff_hh_data=ff_hh_data[ff_hh_data_list]

ff_new_names={'GTCBSA':'CBSA','GESTFIPS':'FIPS','GTCO':'County'}

ff_hh_data=ff_hh_data.rename(columns=ff_new_names)

ff_hh_data=ff_hh_data.dropna()

#This is the section where variables are chosen from the whole data set, so that we don't have to work with all of the information.
#The list is how the variables are chosen and the dictionary is there in case users want to rename the variables.
#the .dropna() is there to get rid of rows with missing information since that means there wasn’t an individual in the family information CSV with the specific household information
#%%
ff_hh_data['FHID']=ff_hh_data['FH_SEQ']+ff_hh_data['FFPOS']

ff_hh_data=ff_hh_data.drop_duplicates(subset='FHID')

ff_hh_data['County']=ff_hh_data['County'].str.zfill(3)

#ff_hh_data['FHID'] was done to identify unique families within the information for better tracking purposes
#ff_hh_data['County'] was created because the County information was not properly put into the CSV from the ASEC, so this fixes this mistake
#Duplicate FHIDs were dropped because the information is from 2019-2021 and there could be instances where we have the same individual from multiple years.
#%%

ff_hh_data['GEOID']=ff_hh_data['FIPS']+ff_hh_data['County']

ff_hh_data.set_index('FHID', inplace=True)

#GEOID was created in case users wanted to map the data in the merged file
#The FHID was set as an index to make it easier to keep track of the information
#%%
ff_hh_data.to_csv('ff_hh_data.csv')
#Now we have a csv to work with for analysis in the other scripts, or for other uses in the future.
