import random

class Hero:
    def __init__(self, name, health=100, attack_power=20, defense=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, other):
        """Атакует другого героя."""
        damage = max(0, self.attack_power - other.defense)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def heal(self):
        """Лечит себя."""
        heal_amount = 15
        self.health += heal_amount
        print(f"{self.name} восстанавливает {heal_amount} здоровья!")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

class Game:
    def __init__(self):
        print("Добро пожаловать в игру 'Битва героев'!")
        player_name = input("Введите имя вашего героя: ")
        self.player = self.create_hero(player_name)
        self.computer = self.create_computer_hero()

    def create_hero(self, name):
        """Создаёт героя с настройкой характеристик."""
        print("Настройте характеристики вашего героя:")
        health = int(input("Введите здоровье (рекомендуется 100): "))
        attack_power = int(input("Введите силу атаки (рекомендуется 20): "))
        defense = int(input("Введите защиту (рекомендуется 10): "))
        return Hero(name=name, health=health, attack_power=attack_power, defense=defense)

    def create_computer_hero(self):
        """Создаёт героя для компьютера на основе уровня сложности."""
        print("Выберите уровень сложности:")
        print("1 - Лёгкий")
        print("2 - Средний")
        print("3 - Сложный")
        difficulty = int(input("Введите уровень сложности (1-3): "))
        if difficulty == 1:
            return Hero(name="Компьютер", health=80, attack_power=15, defense=5)
        elif difficulty == 2:
            return Hero(name="Компьютер", health=100, attack_power=20, defense=10)
        else:
            return Hero(name="Компьютер", health=120, attack_power=25, defense=15)

    def start(self):
        """Начинает игру."""
        print("Игра началась! Ваш герой сразится с компьютером в пошаговом бою.")
        print("В каждом раунде вы можете выбрать действие: атаковать, лечиться или пропустить ход.")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"Поздравляем, {self.player.name} побеждает!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"К сожалению, {self.computer.name} побеждает. Попробуйте снова!")
                break

        print("Игра окончена.")

    def player_turn(self):
        """Ход игрока."""
        print("\nВаш ход! Введите действие:")
        print("'a' - Атаковать противника")
        print("'h' - Восстановить здоровье")
        print("'s' - Пропустить ход")
        action = input("Выберите действие: ").strip().lower()
        if action == 'a':
            self.player.attack(self.computer)
        elif action == 'h':
            self.player.heal()
        elif action == 's':
            print(f"{self.player.name} пропускает ход!")
        else:
            print("Неверный ввод! Вы пропустили ход.")
        self.show_health()

    def computer_turn(self):
        """Ход компьютера."""
        print("\nХод компьютера!")
        action = random.choice(['attack', 'heal'])
        if action == 'attack':
            self.computer.attack(self.player)
        elif action == 'heal':
            self.computer.heal()
        self.show_health()

    def show_health(self):
        """Выводит текущее здоровье героев."""
        print(f"\n{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")

if __name__ == "__main__":
    game = Game()
    game.start()

