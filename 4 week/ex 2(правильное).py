import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig=plt.figure(figsize = (25,20)) # создали рисунок/Figure Fig пропорциями 16:9
ax1=fig.add_subplot(411) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2=fig.add_subplot(412) # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков
ax3=fig.add_subplot(413)
ax4=fig.add_subplot(414)
# сгенерируем данные для какой-нибудь гистограммы
values = np.random.normal(0, 10, 1000)
 
# строим гистограмму с 50 блоками
ax1.hist(values, 150)
ax1.grid() # делаем сетку на графике ax1
ax2.hist(values, 100)
ax2.grid()
ax3.hist(values, 200)
ax3.grid()
ax4.hist(values, 300)
ax4.grid()
plt.show()