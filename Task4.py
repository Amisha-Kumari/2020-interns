# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:06:27 2020

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime as d

first = '2019-01-01'
last = '2019-01-31'

url1='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(first,last)
url2='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'

r1 = requests.get(url1)
data = r1.json()

r2 = requests.get(url2)
latest= r2.json()

values=sorted(data['rates'])

valueINR=[]
valueGBP=[]
date=[]

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
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

