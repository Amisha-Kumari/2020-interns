# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:07:23 2020

@author: Lenovo
"""


import json
import matplotlib.pyplot as plt 
import collections
from datetime import datetime as d
import numpy as np

with open('data.json') as f:
    data = json.load(f)
    
with open('latest-rates.json') as f:
    latest = json.load(f)

first=d(2019,1,1)
last=d(2019,1,31)

values = data["rates"]
values =collections.OrderedDict(sorted(values.items()))

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
plt.ylabel('Value of INR wrt EUR')
plt.title('Exchange rate of INR against EUR')
l=plt.legend(loc="center right")
l.get_texts()[0].set_text("INR="+str(latest['rates']['INR']))
l.get_texts()[1].set_text("GBP="+str(latest['rates']['GBP']))
plt.show()

