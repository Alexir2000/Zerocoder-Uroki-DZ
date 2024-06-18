from uroki.Urok43_VD07_autorization.app import db, app
from uroki.Urok43_VD07_autorization.app.models import User
import sqlite3

# Функция для запуска создания базы
def create_base():
    with app.app_context():
        db.create_all()

def print_base():
    # Путь к базе данных
    db_path = 'instance/site.db'
    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Выполняем запрос к таблице User
    cursor.execute("SELECT id, username, email, password FROM User")
    users = cursor.fetchall()
    # Проходим по всем пользователям и выводим их на экран
    print(" \n Содержимое базы данных USER:")
    n=1
    for user in users:
        print(f'{n}) User: {user[1]}, Email: {user[2]}')
        n += 1
    # Закрываем соединение с базой данных
    conn.close()


# Запускаем создание базы. Только один раз, а потом комментируем.
# create_base()

# Запускаем печать базы для проверки, комментируем если не нужно
print_base()