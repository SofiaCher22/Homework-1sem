import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,25)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(611) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax6 = fig.add_subplot(616)

# сгенерируем данны
 

x = df['SepalLengthCm']
y = df['SepalWidthCm']
k = df['PetalLengthCm']
l = df['PetalWidthCm']

ax1.plot(x,y,'b.', label = 'blue dots')
ax2.plot(x,k,'b.', label = 'blue dots')
ax3.plot(x,l,'b.', label = 'blue dots')
ax4.plot(y,k,'b.', label = 'blue dots')
ax5.plot(y,l,'b.', label = 'blue dots')
ax6.plot(k,l,'b.', label = 'blue dots')
ax1.set_title('first graph')
ax2.set_title('second graph')
ax3.set_title('third graph')
ax4.set_title('forth graph')
ax5.set_title('fifth graph')
ax6.set_title('sixth graph') #здесь название функции немного отличается от случая, когда мы вызывали напрямую из plt!

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid() # делаем сетку на графике ax2
ax2.legend()
ax1.legend()
ax3.legend()
ax4.legend()
ax5.legend()
ax6.legend() # делаем легенду на графике ax2

plt.show()