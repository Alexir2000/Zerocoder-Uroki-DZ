from flask import render_template, request, redirect, url_for
from markupsafe import Markup
# К оригинальному импорту добавился последний - Markup -
# для создания собсвенного фильтра чтобы выдавались переносы строк

from uroki.Urok42_VD06_Forms.app import app

# инициализируем будущий список анкет и задаем имя шаблону для страницы
spisok_anket = []
template1 = "anketa_dz.html"

# Тут мы создаем свою функцию чтобы менять перенос строки \n на <br>
# Иначе мы вводим в поле хобби текст красивый с переводом строк,
# а на выходе получаем все в одну строку -переносы строк исчезают - непорядок
def nl2br(value):
    return Markup(value.replace("\n", "<br>"))

# А Тут мы создаем фильтр замены перевода строки на br - ПРИГОДИТСЯ!
app.jinja_env.filters['nl2br'] = nl2br

# Задаем реакцию в браузере на адреса страниц
@app.route("/", methods=["GET", "POST"])
def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        #функция request.form извлекает значение из соответствующих полей
        name_user = request.form.get('name_user')
        gorod = request.form.get('gorod')
        hobby = request.form.get('hobby')
        vozrast = request.form.get('vozrast')
        # создаёт условие для проверки наличия данных в
        # полях title и content и возраст. хобби не обязательное поле
        if name_user and gorod and vozrast:
            if not hobby:
                hobby = 'Нет хобби'
            add_anketa = {
                'name_user': name_user,
                'gorod': gorod,
                'hobby': hobby,
                'vozrast': vozrast
            }
            # Добавляем анкету в список анкет
            spisok_anket.append(add_anketa)
            #использует для обновления страницы и предотвращения повторной отправки формы.
            return redirect(url_for('index'))
    #возвращает отрендеренный шаблон с переданными данными постов
    return render_template(template1, spisok_anket=spisok_anket)


