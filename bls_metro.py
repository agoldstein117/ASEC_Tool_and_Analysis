# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:28:27 2022

@author: zev11
"""
import pandas as pd

metro = pd.read_csv('metro_codes.txt',sep='\t')

area_codes=metro['area_code']

area=area_codes.to_list()