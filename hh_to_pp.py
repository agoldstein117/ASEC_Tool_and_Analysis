# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:09:04 2022

@author: zev11
"""

import pandas as pd
#I imported pandas here because this tool works with data frames

pppub21=pd.read_csv('pppub21.csv',dtype=str)
pppub20=pd.read_csv('pppub20.csv',dtype=str)
pppub19=pd.read_csv('pppub19.csv',dtype=str)

hhpub21=pd.read_csv('hhpub21.csv',dtype=str)
hhpub20=pd.read_csv('hhpub20.csv',dtype=str)
hhpub19=pd.read_csv('hhpub19.csv',dtype=str)

#these are the household and personal CSVs from the ASEC we will be using this to get the information we want to work with.
#%%
hh_person_names={'H_SEQ':'PH_SEQ'}

hh_to_p21=hhpub21.rename(columns=hh_person_names) 
hh_to_p20=hhpub20.rename(columns=hh_person_names)
hh_to_p19=hhpub19.rename(columns=hh_person_names)

#I created the dictionary and renamed the columns in hhpub so we can merge the personal and household CSVs

#%%
pp_hh_21merge=pppub21.merge(hh_to_p21, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_20merge=pppub20.merge(hh_to_p20, on='PH_SEQ', how='right', validate='m:1', indicator=True)
pp_hh_19merge=pppub19.merge(hh_to_p19, on='PH_SEQ', how='right', validate='m:1', indicator=True)

#I merged the data on PH_SEQ because that is the connector the ASEC uses to match household and personal information
#%%

pp_hh_concact_list=[pp_hh_21merge,pp_hh_20merge,pp_hh_19merge]


pp_hh_data=pd.concat(pp_hh_concact_list)


pp_hh_data=pp_hh_data.drop(columns='_merge')

#I made the list pp_hh_concact_list so I can concatenate the information from 2019-2021, and then dropped the merge indicator since we don't need it.

#%%
pp_hh_data_list=['PH_SEQ','PPPOS','GTCBSA','GESTFIPS','GTCO','GEDIV','PRDTRACE','A_SEX',"A_EXPLF",'A_LFSR','A_MJOCC']

pp_hh_data=pp_hh_data[pp_hh_data_list]

pp_new_names={'GTCBSA':'CBSA','GESTFIPS':'FIPS','GTCO':'County','GEDIV':'Region','PRDTRACE':'Race','A_SEX':'Sex',"A_EXPLF":'Unempoyment_Status','A_LFSR':'In_Labor_Force','A_MJOCC':'Occupation_Type'}

pp_hh_data=pp_hh_data.rename(columns=pp_new_names)

pp_hh_data=pp_hh_data.dropna()

#This is the section where variables are chose from the whole data set, so that we don't have to work with all of the information.
#The list is how the variables are chosen and the dictionary is there in case users want to rename the variables.
#the .dropna() is there to get rid of rows with missing information since that means there wasn’t an individual in the personal information CSV with the specific household information
#%%
pp_hh_data['PSID']=pp_hh_data['PH_SEQ']+pp_hh_data['PPPOS']

pp_hh_data['County']=pp_hh_data['County'].str.zfill(3)
#pp_hh_data['PSID'] was done to identify unique individuals within the information for better tracking purposes
#pp_hh_data['County'] was created because the County information was not properly put into the CSV from the ASEC, so this fixes that mistake
#%%

pp_hh_data['GEOID']=pp_hh_data['FIPS']+pp_hh_data['County']

pp_hh_data=pp_hh_data.drop_duplicates(subset='PSID')

pp_hh_data.set_index('PSID', inplace=True)
#GEOID was created in case users wanted to map the data in the merged file
#Duplicate PSIDs were dropped because the information is from 2019-2021 and there could be instances where we have the same individual from multiple years.
#I did this so we only have information from unique individuals
#The PSID was set as an index to make it easier to keep track of the information

#%%
pp_hh_data.to_csv('pp_hh_data.csv')

#Now we have a csv to work with for analysis in the other scripts, or for other uses in the future.
