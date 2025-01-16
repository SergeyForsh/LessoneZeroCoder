from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретный класс для меча
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

# Конкретный класс для лука
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            raise TypeError("Оружие должно быть экземпляром класса Weapon")

    def attack(self, monster):
        if self.weapon:
            attack_result = self.weapon.attack()
            print(attack_result)
            monster.take_damage()
        else:
            print("Боец без оружия не может атаковать!")

# Класс монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} получил урон, осталось здоровья: {self.health}")

# Демонстрация работы
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Герой")
    monster = Monster("Гоблин", 1)

    # Выбираем меч
    sword = Sword()
    fighter.change_weapon(sword)
    print("Боец выбирает меч.")
    fighter.attack(monster)

    # Создаем нового монстра
    monster = Monster("Орк", 2)

    # Выбираем лук
    bow = Bow()
    fighter.change_weapon(bow)
    print("Боец выбирает лук.")
    fighter.attack(monster)
    fighter.attack(monster)
