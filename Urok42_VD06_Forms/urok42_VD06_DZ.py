
"""
Создайте веб-приложение на Flask, которое включает форму для
ввода данных о пользователе
в анкету
(имя,
 город,
 хобби
 и возраст).
После отправки формы отображайте введенные данные на той же странице.
Внимает он привычным ухом
Свист;
Марает он единым духом
Лист;
Потом всему терзает свету
Слух;
Потом печатает — и в Лету
Бух!
"""

# Прописываем путь в ини файле до app начиная от корня проекта через точку
# Нельзя задавать имена папкам и файлам с тире - не будет работать!

from uroki.Urok42_VD06_Forms.app import app
from app import routes_dz # подключаем файл с дз

if __name__ == "__main__":
    app.run(debug=True)
