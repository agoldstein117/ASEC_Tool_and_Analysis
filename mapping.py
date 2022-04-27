# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:11:02 2022

@author: zev11
"""

import pandas as pd
import geopandas as gpd

cbsamap=gpd.read_file('cb_2020_us_cbsa_500k.zip')

cbsamap=cbsamap.rename(columns={'CBSAFP':'GTCBSA'})
