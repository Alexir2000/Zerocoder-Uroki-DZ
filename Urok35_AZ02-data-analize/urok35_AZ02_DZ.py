import pandas as pd
import random


def create_data():
    data_fio = ['Иванов','Сидоров', 'Петров', 'Васечкин', 'Степанов',
                            'Павлов','Соколов','Орлов','Сидоров','Кузнецов']
    data_predmet = ['Математика', 'Физика', 'Информатика', 'Русский язык', 'Литература']
    data_ocenka = [2,3,3,3,3,4,4,4,4,4,4,5,5,5]
    num_rows = 50

    new_data = {
        'ФИО': [random.choice(data_fio) for _ in range(num_rows)],
        'Предмет': [random.choice(data_predmet) for _ in range(num_rows)],
        'Оценка': [random.choice(data_ocenka) for _ in range(num_rows)]
    }
    return new_data
def get_iqr(df_value):
    q1 = df_value.quantile(0.25)
    q3 = df_value.quantile(0.75)
    iqr = q3 - q1
    dowside = q1 - 1.5 * iqr
    upside = q3 + 1.5 * iqr
    result = {
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Downside": dowside,
        "Upside": upside,
    }
    return result
def save_data(file_name,data):
    pd_new = pd.DataFrame(data)
    pd_new.to_csv(file_name, index=False, encoding='utf-8')

file_name = "data-dz.csv"

# data = create_data() # здесь однократно создались случайные данные для создания датафрейма
# save_data(file_name,data) # здесь создался файл с данными из которого будм считывать далее

df = pd.read_csv(file_name)

print("\n HEAD:")
print(df.head())

print("\n INFO:")
print(df.info())

print("\n DESCRIBE:")
print(df.describe())

srednee_po_predmetam = df.groupby('Предмет')['Оценка'].mean()
median_po_predmetam = df.groupby('Предмет')['Оценка'].median()
std_po_predmetam = df.groupby('Предмет')['Оценка'].std()

print(f"\n Средняя оценка по предметам \n {srednee_po_predmetam}")
print(f"\n Медианная оценка по предметам \n {median_po_predmetam}")
print(f"\n Среднее отклонение оценки по предметам \n {std_po_predmetam}")

print(f" \n Средняя оценка по математике: {srednee_po_predmetam['Математика']:.2f}")
print(f" Среднее отклонение оценки по математике: {std_po_predmetam['Математика']:.2f}")

df_matem = df[df['Предмет'] == 'Математика']
iqr_matem = get_iqr(df_matem["Оценка"]) # получение расчета переменных q1 q3 iqr

print(f"\n Q1 по математике: {iqr_matem['Q1']:.2f} "
      f"\n Q3 по математике: {iqr_matem['Q3']:.2f} "
      f"\n IQR по математике: {iqr_matem['IQR']:.2f}"
      f"\n Downside по математике: {iqr_matem['Downside']:.2f}"
      f"\n Upside по математике: {iqr_matem['Upside']:.2f}")




