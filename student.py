# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# - можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонение

#Импортируем библиотеу
import pandas as pd


#Создаем датасет
subjects = ["Математика", "Физика", "Химия", "Биология","Русский"]
data = {
    "Ученик": ["Петров", "Иванов", "Сидоров", "Борисов", "Ефимов", "Федоров", "Александров", "Костиков", "Глебов", "Захаров"],
    subjects[0]: [3, 4, 5, 5, 4, 4, 5, 3, 2, 5],
    subjects[1]: [4, 4, 4, 5, 3, 3, 4, 5, 3, 5],
    subjects[2]: [5, 4, 3, 2, 3, 4, 5, 4, 3, 5],
    subjects[3]: [3, 4, 5, 5, 4, 3, 4, 5, 4, 5],
    subjects[4]: [2, 3, 4, 5, 5, 4, 3, 3, 4, 5]
}

#Создаем датафрейм
df = pd.DataFrame(data)

#Смотрим первые 5 записей
print(df.head())

#Выводим медианные оценки по предметам
print("\nСредние оценки по предметам")
for subject in subjects:
    print(f"{subject}: {df[subject].mean()}")

#Выводим средние оценки по предметам
print("\nМедианные оценки по предметам")
for subject in subjects:
    print(f"{subject}: {df[subject].median()}")

#Вычисляем квартили Q1 и Q3 для оценок по математике:
Q1_math = df[subjects[0]].quantile(0.25)
Q3_math = df[subjects[0]].quantile(0.75)

#Рассчитываем межквартильный размах для оценок по математике
IQR_math = Q3_math - Q1_math

#Выводим квартили Q1 и Q3 и межквартильный размах для оценок по математике
print(f"\nПервая квартиль для оценок по математике равна: {Q1_math}")
print(f"Третья квартиль для оценок по математике равна: {Q3_math}")
print(f"Межквартильный размах для оценок по математике равен: {IQR_math}")

#Выводим стандартные отклонения по предметам
print("\nСтандартные отклонения по предметам")
for subject in subjects:
    print(f"{subject}: {df[subject].std()}")