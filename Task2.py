# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:35:25 2020

@author: Lenovo
"""


import json
import matplotlib.pyplot as plt 
from datetime import datetime as d
import numpy as np

with open('data.json') as f:
    data = json.load(f)

first=d(2019,1,1)
last=d(2019,1,31)

values = sorted(data["rates"])

valueINR=[]
valueGBP=[]
date=[]

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
    if day <= last and day >= first:
        valueINR+=[data['rates'][i]['INR']]
        valueGBP+=[data['rates'][i]['GBP']]
        date+=[day.day]
        
plt.plot(date,valueINR, linewidth=2, linestyle='solid', color='blue', label='INR')
plt.plot(date,valueGBP, linewidth=2, linestyle='solid', color='red', label='GBP')

plt.xlabel('January 2019')
plt.xticks(np.arange(32),rotation=45)
plt.ylabel('Value wrt EUR')
plt.title('Exchange rate against EUR')
plt.legend()
plt.show()
