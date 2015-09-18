# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:38:59 2015

@author: architgupta
"""

import pandas as pd
df = pd.read_csv("irish_cities.txt", sep="\t", skiprows=1)
df["Population (2000)"] /= 1000000.0
df.head