df = pd.read_csv('iris_data.csv')
df
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('iris_data.csv')
print(data.head())
species_counts = data['Species'].value_counts()
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1) 
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Доля разных видов ирисов')


length_counts = [
    data[data['PetalLengthCm'] > 1.2].shape[0],  # больше 1.2 см
    data[(data['PetalLengthCm'] > 1.2) & (data['PetalLengthCm'] < 1.5)].shape[0],  # больше 1.2 и меньше 1.5 см
    data[data['PetalLengthCm'] > 1.5].shape[0]   # больше 1.5 см
]

length_labels = ['> 1.2 см', '1.2-1.5 см', '> 1.5 см']
plt.subplot(1, 2, 2)  
plt.pie(length_counts, labels=length_labels, autopct='%1.1f%%', startangle=90)
plt.title('Доля ирисов по длине лепестка')

plt.tight_layout()
plt.savefig('iris_pie_charts.png', dpi=300)
plt.show()