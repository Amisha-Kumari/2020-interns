
import matplotlib.pyplot as plt
import requests

first = input('Enter start date (yyyy-mm-dd):')
last = input('Enter last date (yyyy-mm-dd):')

cur1=input('Enter 1st currency (eg- INR):')
cur2=input('Enter 2nd currency (eg- USD):')

url1='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={},{}'.format(first,last,cur1,cur2)
url2='https://api.exchangeratesapi.io/latest?symbols={},{}'.format(cur1,cur2)

r1 = requests.get(url1)
data = r1.json()

r2 = requests.get(url2)
latest= r2.json()

values=sorted(data['rates'])

value1=[]
value2=[]
date=[]

for i in values:    
    value1+=[data['rates'][i][cur1]]
    value2+=[data['rates'][i][cur2]]
    date+=[i]
        
plt.plot(date,value1, linewidth=2, linestyle='solid', color='blue', label='INR')
plt.plot(date,value2, linewidth=2, linestyle='solid', color='red', label='GBP')

plt.xlabel('Time Period')
plt.xticks(rotation=45)
plt.ylabel('Value of currencies wrt EUR')
plt.title('Exchange rate of currencies against EUR')
l=plt.legend(loc="center right")
l.get_texts()[0].set_text(cur1+str(latest['rates'][cur1]))
l.get_texts()[1].set_text(cur2+str(latest['rates'][cur2]))
plt.show()
