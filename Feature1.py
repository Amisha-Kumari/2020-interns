import matplotlib.pyplot as plt
import requests

first = input('Enter start date (yyyy-mm-dd):')
last = input('Enter last date (yyyy-mm-dd):')

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
    valueINR+=[data['rates'][i]['INR']]
    valueGBP+=[data['rates'][i]['GBP']]
    date+=[i]
        
plt.plot(date,valueINR, linewidth=2, linestyle='solid', color='blue', label='INR')
plt.plot(date,valueGBP, linewidth=2, linestyle='solid', color='red', label='GBP')

plt.xlabel('Time Period')
plt.xticks(rotation=45)
plt.ylabel('Value of currencies wrt EUR')
plt.title('Exchange rate of currencies against EUR')
l=plt.legend(loc="center right")
l.get_texts()[0].set_text("INR="+str(latest['rates']['INR']))
l.get_texts()[1].set_text("GBP="+str(latest['rates']['GBP']))
plt.show()

