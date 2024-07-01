import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
house_data = pd.read_csv('путь_к_вашему_файлу/kc-house-data.csv')
laptop_data = pd.read_csv('/mnt/data/laptop_price (1) (1).csv')

# Вывод первых строк данных
print(house_data.head())
print(laptop_data.head())

# Распределение жилой площади
plt.figure(figsize=(10, 6))
sns.histplot(house_data['sqft_living'], bins=30, kde=True)
plt.title('Распределение жилой площади')
plt.xlabel('Квадратура (кв. футы)')
plt.ylabel('Частота')
plt.show()

# Распределение года постройки
plt.figure(figsize=(10, 6))
sns.histplot(house_data['yr_built'], bins=30, kde=True)
plt.title('Распределение года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Частота')
plt.show()

# Распределение домов от наличия вида на набережную
plt.figure(figsize=(10, 6))
sns.countplot(x='waterfront', data=house_data)
plt.title('Распределение домов с видом на набережную')
plt.xlabel('Наличие вида на набережную (0 - нет, 1 - да)')
plt.ylabel('Частота')
plt.show()

# Распределение этажей домов
plt.figure(figsize=(10, 6))
sns.countplot(x='floors', data=house_data)
plt.title('Распределение этажей домов')
plt.xlabel('Количество этажей')
plt.ylabel('Частота')
plt.show()

# Распределение состояния домов
plt.figure(figsize=(10, 6))
sns.countplot(x='condition', data=house_data)
plt.title('Распределение состояния домов')
plt.xlabel('Состояние дома')
plt.ylabel('Частота')
plt.show()

# Исследование характеристик недвижимости, влияющих на стоимость
# Жилая площадь
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqft_living', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от жилой площади')
plt.xlabel('Жилая площадь (кв. футы)')
plt.ylabel('Стоимость')
plt.show()

# Год постройки
plt.figure(figsize=(10, 6))
sns.scatterplot(x='yr_built', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Стоимость')
plt.show()

# Состояние дома
plt.figure(figsize=(10, 6))
sns.scatterplot(x='condition', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от состояния дома')
plt.xlabel('Состояние дома')
plt.ylabel('Стоимость')
plt.show()

# Количество спален
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bedrooms', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от количества спален')
plt.xlabel('Количество спален')
plt.ylabel('Стоимость')
plt.show()

# Площадь участка
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqft_lot', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от площади участка')
plt.xlabel('Площадь участка (кв. футы)')
plt.ylabel('Стоимость')
plt.show()
# Пример для зависимости стоимости недвижимости от жилой площади
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqft_living', y='price', data=house_data)
plt.title('Зависимость стоимости недвижимости от жилой площади')
plt.xlabel('Жилая площадь (кв. футы)')
plt.ylabel('Стоимость')
plt.show()

print("На диаграмме зависимости стоимости недвижимости от жилой площади видно, что с увеличением площади стоимость также растет, что логично, так как большие дома обычно стоят дороже. Наиболее высокие значения стоимости наблюдаются для площадей более 4000 кв. футов.")
