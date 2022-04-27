# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:36:13 2022

@author: zev11
"""
import requests
import json
import pandas as pd

metro = pd.read_csv('metro_codes.txt',sep='\t')

metro['LAU']='LAU'

metro['Measure Code']='03'

id_list=['LAU','area_code','Measure Code','area_text']

series_ids=metro[id_list]

#%%

series_id=series_ids['LAU']+series_ids['area_code']+series_ids['Measure Code']

series_ids= series_id.to_list()


#31080

#%%
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid":series_ids,"startyear":"2021", "endyear":"2021"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
res=json_data['Results']
series_list=res['series']

#%%
for s in series_list:
    ID= s['seriesID']
    data=s['data']
    data=pd.DataFrame(data)
    print(ID,data)
    
data['seriesID']=ID
