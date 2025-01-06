class User:
    """
    Класс User инкапсулирует данные о пользователе: ID, имя и уровень доступа.
    """
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Setters (только для имени, ID и уровень доступа обычно не изменяются)
    def set_name(self, name):
        self._name = name

    def __repr__(self):
        return f"User(ID={self._user_id}, Name={self._name}, AccessLevel={self._access_level})"

class Admin(User):
    """
    Класс Admin наследуется от User и добавляет возможность управления списком пользователей.
    """
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')

    def add_user(self, user_list, new_user):
        """
        Добавляет нового пользователя в список пользователей.
        :param user_list: Список существующих пользователей
        :param new_user: Экземпляр класса User, который нужно добавить
        """
        if not isinstance(new_user, User):
            raise ValueError("new_user должен быть экземпляром класса User")
        user_list.append(new_user)

    def remove_user(self, user_list, user_id):
        """
        Удаляет пользователя по ID из списка пользователей.
        :param user_list: Список существующих пользователей
        :param user_id: ID пользователя, которого нужно удалить
        """
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                return
        raise ValueError(f"Пользователь с ID {user_id} не найден")

    def __repr__(self):
        return f"Admin(ID={self._user_id}, Name={self._name}, AccessLevel={self._access_level})"

# Пример использования
if __name__ == "__main__":
    # Создаем список пользователей
    users = []

    # Создаем администратора
    admin = Admin(user_id=1, name="AdminUserСергей")

    # Добавляем пользователей через администратора
    user1 = User(user_id=2, name="Елена")
    user2 = User(user_id=3, name="Александр")
    user3 = User(user_id=4, name="Денис")
    user4 = User(user_id=5, name="Владимир")
    user5 = User(user_id=6, name="Олег")

    admin.add_user(users, user1)
    admin.add_user(users, user2)
    admin.add_user(users, user3)
    admin.add_user(users, user4)
    admin.add_user(users, user5)

    print("Список пользователей после добавления:", users)

    # Удаляем пользователя через администратора
    admin.remove_user(users, user_id=2)

    print("Список пользователей после удаления:", users)

    # Демонстрация инкапсуляции
    print("Имя пользователя 3:", user2.get_name())
    user2.set_name("Дмитрий")
    print("Обновленное имя пользователя 3:", user2.get_name())
