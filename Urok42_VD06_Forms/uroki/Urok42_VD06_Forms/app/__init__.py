from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "yuo-will-never-guess"
from uroki.Urok42_VD06_Forms.app import routes_dz
# Прописываем путь в ини файле до app начиная от корня проекта через точку
# Нельзя задавать имена папкам и файлам с тире - не будет работать!

