import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя."""
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

class Game:
    def __init__(self):
        print("Добро пожаловать в игру 'Битва героев'!")
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(name=player_name)
        self.computer = Hero(name="Компьютер")

    def start(self):
        """Начинает игру."""
        print("Игра началась! Ваш герой сразится с компьютером в пошаговом бою.")
        print("В каждом раунде вы можете выбрать действие: атаковать или пропустить ход.")
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
        print("'s' - Пропустить ход")
        action = input("Выберите действие: ").strip().lower()
        if action == 'a':
            self.player.attack(self.computer)
        elif action == 's':
            print(f"{self.player.name} пропускает ход!")
        else:
            print("Неверный ввод! Вы пропустили ход.")
        self.show_health()

    def computer_turn(self):
        """Ход компьютера."""
        print("\nХод компьютера!")
        self.computer.attack(self.player)
        self.show_health()

    def show_health(self):
        """Выводит текущее здоровье героев."""
        print(f"\n{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")

if __name__ == "__main__":
    game = Game()
    game.start()
