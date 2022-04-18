# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:11:02 2022

@author: zev11
"""

import pandas as pd
import geopandas as gpd

cbsamap=gpd.read_file('cb_2020_us_cbsa_500k.zip')

cbsamap=cbsamap.rename(columns={'CBSAFP':'GTCBSA'})

UI_map=cbsamap.merge(concact_full_data, on='GTCBSA', how='left', validate='m:1', indicator=True)

concact_full_data.to_csv('final_data.csv')