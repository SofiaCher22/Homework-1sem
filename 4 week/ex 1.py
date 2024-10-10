import matplotlib.pyplot as plt
import numpy as np
x = [63.08, 68.7, 74.83, 79.83, 89.38, 94.95, 104.94, 128.13, 146.95]
y = [315, 345, 375, 400, 445, 480, 525, 645, 735]
plt.figure(figsize=(8, 5), dpi=100)
plt.plot(x, y, 'b^--')
plt.title('Результаты измерений напряжения в зависимости от силы тока',
          fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('Ia, мА')
plt.ylabel('Vb, мВ')
plt.xticks([60, 80, 100, 120, 140, 160])
plt.yticks([300, 400, 500, 600, 700, 800])
plt.grid()
plt.savefig('mygraph.png', dpi=300)
plt.show()