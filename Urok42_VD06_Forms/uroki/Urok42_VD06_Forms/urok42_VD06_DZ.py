
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
# Так как у нас проект находится не в корне,
# то задаем путь к app через подпапки и  вместо слеша будет точка
from uroki.Urok42_VD06_Forms.app import app

if __name__ == "__main__":
    app.run(debug=True)