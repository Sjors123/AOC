# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:48:53 2020

@author: esdeb
"""
import numpy as np
data = np.loadtxt('dataset1.txt')

for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        result = data[i]+data[j]
        if result == 2020:
            print(data[i])
            print(data[j])
            final_result=data[i]*data[j]
print(final_result)            