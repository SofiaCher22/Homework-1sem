import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('BTC_data.csv')
number = list(df['time'])
price = list(df['close'])
for i in range(len(number)):
    number[i] = (number[i])[:10]
price2 = []
for i in range(len(price)):
    price2.append((price[i])**2)
p = np.poly1d(np.polyfit(price, price2, 3))
plt.plot(number, p(price))
plt.title('Аппроксимация цены биткоина полиномом ', fontdict={
          'fontname': 'sans-serif', 'fontsize': 10})
plt.xlabel('Число')
plt.ylabel('Цена')
plt.show()
