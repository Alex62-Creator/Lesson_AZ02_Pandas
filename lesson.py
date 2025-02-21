import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Пример 1 Стандартное отклонение

data = {
    'Набор А': [85, 90, 95, 100, 105],
    'Набор Б': [70, 80, 95, 110, 120],
}

df = pd.DataFrame(data)

#Вычислим стандартное отклонение
stdA = df['Набор А'].std()
stdB = df['Набор Б'].std()
print(f"Стандартное отклонение 1 набор - {stdA}")
print(f"Стандартное отклонение 2 набор - {stdB}")

#Пример 2 Статистические функции

data = {
    'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
}

df = pd.DataFrame(data)

print(df.describe())

print(f"Средний возраст - {df['Возраст'].mean()}")
print(f"Медианный возраст - {df['Возраст'].median()}")
print(f"Стандартное отклонение возраста - {df['Возраст'].std()}")

print(f"Средняя зарплата - {df['Зарплата'].mean()}")
print(f"Медианная зп - {df['Зарплата'].median()}")
print(f"Стандартное отклонение зп - {df['Зарплата'].std()}")

#Пример 3 Временные ряды

#Cоздадим даты с интервалом в один день
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
#Создадим список из случайных значений
values = np.random.rand(10)

#Создадим датафрейм со словарём
df = pd.DataFrame({'Date': dates, 'Value': values})

#Установим колонку Date в качестве индекса всего датафрейма
df.set_index('Date', inplace=True)

#Используем ресэмплирование, чтобы установить новый интервал: раз в месяц
month = df.resample('ME').mean()

print(df)
print(month)

#Пример 4 Обработка выбросов

data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)

#Создадим график
df['value'].hist()
plt.show()
df.boxplot(column='value')
plt.show()

print(df.describe())

#Определим первый (Q1) и третий (Q3) квартили
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)

#Теперь рассчитаем межквартильный размах
IQR = Q3 - Q1

#Определим нижнюю и верхнюю границы для определения выбросов
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

#Удаляем выбросы, которые не входят в очерченный диапазон
df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

#Строим график
df_new.boxplot(column='value')
plt.show()

#Пример 4 Работа с категориальными данными

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

#Преобразуем столбцы в категориальные данные
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

#Просмотрим уникальные категории
print(df['gender'].cat.categories)
print(df['department'].cat.categories)

#Можем также посмотреть числовые коды категорий
print(df['gender'].cat.codes)

#Добавим новую категорию
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

#Удаляем категорию
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print(df)