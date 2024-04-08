

# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять
# или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных:
# Убедись, что атрибуты классов защищены от прямого доступа
# и модификации снаружи. Предоставь доступ к необходимым атрибутам
# через методы (например, get и set методы).
#
# В поле для ответа загрузи ссылку на GitHub-репозиторий,
# содержащий код проекта с реализацией задания.


# def my_function(number: int, text: str)
class User():
    def __init__(self, id:str, name:str, dostup = "user"):
        self.__id = id
        self.__name = name
        self.__uroven_dostupa = dostup
    def print_info_user(self):
        print(f"\n Информация о пользователе - {self.__name}")
        print(f"ID пользователя - {self.__id}")
        print(f"Уровень доступа - {self.__uroven_dostupa}")

    def get_name(self):
        return self.__name
    def set_name(self, name: str):
        self.__name = name
    def get_id(self):
        return self.__id
    def get_dostup(self):
        return self.__uroven_dostupa

    def set_id(self,id:str):
        self.__id = id
    def set_dostup(self,dostup = "user"):
        self.__uroven_dostupa = dostup

class UserUser(User):
    def __init__(self, id:str, name:str):
        super().__init__(id, name)
    def get_id(self):
        return "недоступно"
    def get_dostup(self):
        return "недоступно"
    def set_id(self,id:str):
        pass
    def set_dostup(self,dostup = "user"):
        pass
class AdminUser(User):
    def __init__(self, id:str, name:str, dostup = "admin"):
        super().__init__(id, name, dostup)
    def add_user(self, user_list:list,user:User):
        return user_list.append(user)
    def remove_user(self,user_list:list,user:User):
        return user_list.remove(user)


user1_id = "0001050628"
user1_name = "Петька"

user2_id = "000810500777"
user2_name = "Анка"

user3_id = "77700000333"
user3_name = "Василий Иванович"


user1 = UserUser(user1_id, user1_name)
user1.print_info_user()
user2 = UserUser(user2_id, user2_name)
user3 = AdminUser(user3_id, user3_name)
user3.print_info_user()

print(" \n Проверка доступности инкапсулированных данных...")

user_cur = user1
print(f" \n Пользователь {user_cur.get_name()}: \n ID - {user_cur.get_id()}, Уровень доступа - {user_cur.get_dostup()}")

user_cur = user3
print(f" \n Пользователь {user_cur.get_name()}: \n ID - {user_cur.get_id()}, Уровень доступа - {user_cur.get_dostup()}")

print(" \n Добавление пользователей в список...")
user_list = []
user3.add_user(user_list,user1)
user3.add_user(user_list,user2)
user3.add_user(user_list,user2)
user3.add_user(user_list,user3)

print(" \n Список пользователей:")
for i in user_list:
    print(i.get_name())

user_cur = user2
print(f" \n Удаление пользователя {user_cur.get_name()} ...")
user3.remove_user(user_list,user_cur)

print(" \n Список пользователей:")
for i in user_list:
    print(i.get_name())






