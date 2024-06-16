import pandas as pd

file_name = "players_3120.csv"
df = pd.read_csv(file_name)

print("\n HEAD:")
print(df.head())

print("\n INFO:")
print(df.info())

print("\n DESCRIBE:")
print(df.describe())

print("\n ЗАПИСЬ ИНДЕКС 1")
print(df.loc[1])

file_name2 = "dz.csv"
df2 = pd.read_csv(file_name2)

print(f"\n INFO из файла {file_name2}:")
print(df2.info())

group = df2.groupby('City')['Salary'].mean()
print(f"\n Средняя зарплата из файла {file_name2}:")
print(group)

