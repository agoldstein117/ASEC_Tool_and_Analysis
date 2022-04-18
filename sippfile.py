# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:49:59 2022

@author: zev11
"""

#Import the pandas module. This code requires version 0.24 or higher
#	in order to use the Int64 and Float64 data types, which allow for
#	missing values
import pandas as pd

#Read in the primary data file schema to get data-type information for
#	each variable.
rd_schema = pd.read_csv('pu2020_csv.zip')



