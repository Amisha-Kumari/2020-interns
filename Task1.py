# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 06:35:59 2020

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

value=[]
date=[]

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
    if day <= last and day >= first:
        value+=[data['rates'][i]['INR']]
        date+=[day.day]
        
plt.plot(date,value,'go--', linewidth=2, linestyle='solid', color='blue')
plt.xlabel('January 2019')
plt.xticks(np.arange(32),rotation=45)
plt.ylabel('Value of INR wrt EUR')
plt.title('Exchange rate of INR against EUR')
plt.show()
