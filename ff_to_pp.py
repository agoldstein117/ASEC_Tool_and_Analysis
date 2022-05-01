# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:13:43 2022

@author: zev11
"""
import pandas as pd


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


pp_ff_data_list=['PH_SEQ','PPPOS','PRDTRACE','A_SEX']

pp_ff_data=pp_ff_data[pp_ff_data_list]

ff_new_names={'PRDTRACE':'Race','A_SEX':'Sex'}

pp_ff_data=pp_ff_data.rename(columns=ff_new_names)

pp_ff_data=pp_ff_data.dropna()

pp_ff_data['PSID']=pp_ff_data['PH_SEQ']+pp_ff_data['PPPOS']

pp_ff_data=pp_ff_data.drop_duplicates(subset='PSID')

pp_ff_data.set_index('PSID', inplace=True)

#%%
pp_ff_data.to_csv('ff_pp_data.csv')