# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound должен быть переопределен в подклассах.")

    def eat(self):
        print(f"{self.name} ест.")

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return "Чирик!"

# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return "Р-р-р!"

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return "Ш-ш-ш!"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, возраст: {animal.age}")

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Попугай", 2)
    tiger = Mammal("Тигр", 5)
    snake = Reptile("Змея", 3)

    # Демонстрация полиморфизма
    animal_sound([parrot, tiger, snake])

    # Создание зоопарка
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)

    # Создание сотрудников
    zookeeper = ZooKeeper("Иван")
    veterinarian = Veterinarian("Мария")

    # Добавление сотрудников в зоопарк
    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    # Отображение животных в зоопарке
    zoo.show_animals()

    # Кормление и лечение животных
    zookeeper.feed_animal(parrot)
    veterinarian.heal_animal(tiger)


    ### Объяснение кода:
    # 1. ** Базовый класс `Animal`: Содержит общие атрибуты `name` и `age`,
    # а также методы `make_sound()` и `eat()`.
    # 2. ** Подклассы **: `Bird`, `Mammal` и `Reptile` наследуются от `Animal` и переопределяют
    # метод `make_sound()` для каждого типа животного.
    # 3. ** Полиморфизм **: Функция `animal_sound()` принимает список животных и вызывает для
    # каждого из них метод `make_sound()`.
    # 4. ** Композиция **: Класс `Zoo` содержит списки животных и сотрудников, а также
    # методы для добавления объектов этих классов.
    # 5. ** Сотрудники **: Классы `ZooKeeper` и `Veterinarian` имеют специфические методы
    # для взаимодействия с животными.
    # Этот код демонстрирует основные принципы ООП: наследование, полиморфизм и композицию.
