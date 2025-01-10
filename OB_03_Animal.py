class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} chirps."

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wing_span} meters."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} growls."

    def run(self):
        return f"{self.name} is running."


class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return f"{self.name} hisses."

    def crawl(self):
        return f"{self.name} is crawling."


# Polymorphism

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Composition

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("Only instances of Animal can be added.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def list_animals(self):
        return [animal.name for animal in self.animals]

    def list_staff(self):
        return [staff.name for staff in self.staff]


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            return f"{self.name} is feeding {animal.name}."
        else:
            raise TypeError("Can only feed animals.")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            return f"{self.name} is treating {animal.name}."
        else:
            raise TypeError("Can only treat animals.")


# Demonstration
if __name__ == "__main__":
    # Create animals
    parrot = Bird("Parrot", 2, 0.5)
    lion = Mammal("Lion", 5, "Golden")
    snake = Reptile("Snake", 3, "Diamond")

    # Polymorphism
    animal_sound([parrot, lion, snake])

    # Zoo
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    print("Animals in the zoo:", zoo.list_animals())

    # Staff
    keeper = ZooKeeper("Alice")
    vet = Veterinarian("Dr. Bob")

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    print("Staff in the zoo:", zoo.list_staff())

    # Staff actions
    print(keeper.feed_animal(lion))
    print(vet.heal_animal(snake))

# Этот код предоставляет:
# Базовый класс Animal с общими атрибутами и методами.
# Подклассы Bird, Mammal, Reptile с уникальными атрибутами и методами.
# Полиморфизм: демонстрация работы метода make_sound() через функцию animal_sound.
# Композицию: класс Zoo для управления животными и сотрудниками.
# Сотрудники: классы ZooKeeper и Veterinarian с уникальными методами для работы с животными.