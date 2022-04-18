# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:36:13 2022

@author: zev11
"""
import requests
import json
import pandas as pd

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LAUMTB*'],"startyear":"2019", "endyear":"2021"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
res=json_data['Results']
series_list=res['series']
for s in series_list:
    ID= s['seriesID']
    data=s['data']
    data=pd.DataFrame(data)
    print(ID,data)
    
    
data['seriesID']=ID

metros=pd.read_csv('Metro_codes.csv')

split=metros['codes'].str.split()
split.to_csv('codes_split.csv')