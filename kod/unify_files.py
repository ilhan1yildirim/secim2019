# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:41:59 2019

@author: ilhan
"""

import os
import pandas as pd

MARCH_31_PATH = '../mart_31/'
JUNE_23_PATH = '../haziran_23/'

list_locations = os.listdir(MARCH_31_PATH + 'ilce/')

num_locations = len(list_locations)

frames_march = []
frames_june = []
for i in range(num_locations):
    df = pd.read_excel(MARCH_31_PATH + 'ilce/' + list_locations[i], header=10)
    frames_march.append(df)
    df = pd.read_excel(JUNE_23_PATH + 'ilce/' + list_locations[i], header=10)
    frames_june.append(df)
    
frames_march_uni = pd.concat(frames_march)
frames_june_uni = pd.concat(frames_june)

frames_march_uni.to_csv(MARCH_31_PATH + 'combined.csv')
frames_june_uni.to_csv(JUNE_23_PATH + 'combined.csv')
