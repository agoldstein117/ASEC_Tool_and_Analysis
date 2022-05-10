# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:13:43 2022

@author: zev11
"""
import pandas as pd


pppub21=pd.read_csv('pppub21.csv',dtype=str)
pppub20=pd.read_csv('pppub20.csv',dtype=str)
pppub19=pd.read_csv('pppub19.csv',dtype=str)

ffpub21=pd.read_csv('ffpub21.csv',dtype=str)
ffpub20=pd.read_csv('ffpub20.csv',dtype=str)
ffpub19=pd.read_csv('ffpub19.csv',dtype=str)
#I imported pandas here because this tool works with data frames
#these are the family and personal CSVs from the ASEC we will be using this to get the information we want to work with.
#%%
ff_person_names={'FH_SEQ':'PH_SEQ'}

ff_to_p21=ffpub21.rename(columns=ff_person_names)
ff_to_p20=ffpub20.rename(columns=ff_person_names)
ff_to_p19=ffpub19.rename(columns=ff_person_names)

#I created the dictionary and renamed the columns in ffpub so we can merge the personal and family CSVs
#%%
pp_ff_21merge=pppub21.merge(ff_to_p21, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_20merge=pppub20.merge(ff_to_p20, on='PH_SEQ', how='left', validate='m:m', indicator=True)
pp_ff_19merge=pppub19.merge(ff_to_p19, on='PH_SEQ', how='left', validate='m:m', indicator=True)

#I merged the data on PH_SEQ because that is the connector the ASEC uses to match family and personal information
#%%

pp_ff_concact_list=[pp_ff_21merge,pp_ff_20merge,pp_ff_19merge]

pp_ff_data=pd.concat(pp_ff_concact_list)

pp_ff_data=pp_ff_data.drop(columns='_merge')

#I made the list pp_ff_concact_list so I can concatenate the information from 2019-2021, and then dropped the merge indicator since we don't need it.
#%%

pp_ff_data_list=['PH_SEQ','PPPOS','GTCBSA','GESTFIPS','GTCO','PRDTRACE','A_SEX']

pp_ff_data=pp_ff_data[pp_ff_data_list]
#This is the section where variables are chose from the whole data set, so that we don't have to work with all of the information.
#%%

ff_new_names={'PRDTRACE':'Race','A_SEX':'Sex'}

pp_ff_data=pp_ff_data.rename(columns=ff_new_names)

pp_ff_data=pp_ff_data.dropna()
#The list is how the variables are chosen and the dictionary is there in case users want to rename the variables.
#the .dropna() is there to get rid of rows with missing information since that means there wasn’t an individual in the personal information CSV with the specific family information

#%%
pp_ff_data['PSID']=pp_ff_data['PH_SEQ']+pp_ff_data['PPPOS']

#pp_ff_data['PSID'] was done to identify unique individuals within the information for better tracking purposes
#%%


pp_ff_data=pp_ff_data.drop_duplicates(subset='PSID')

pp_ff_data.set_index('PSID', inplace=True)

#Duplicate PSIDs were dropped because the information is from 2019-2021 and there could be instances where we have the same individual from multiple years.
#I did this so we only have information from unique individuals
#The PSID was set as an index to make it easier to keep track of the information

#%%
pp_ff_data.to_csv('ff_pp_data.csv')

#Now we have a csv to work with for analysis in the other scripts, or for other uses in the future.