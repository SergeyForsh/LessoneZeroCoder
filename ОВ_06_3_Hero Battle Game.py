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
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(name=player_name)
        self.computer = Hero(name="Компьютер")

    def start(self):
        """Начинает игру."""
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

        print("Игра окончена.")

    def player_turn(self):
        """Ход игрока."""
        action = input("Ваш ход! Введите 'a' для атаки: ").strip().lower()
        if action == 'a':
            self.player.attack(self.computer)
        else:
            print("Вы пропустили ход!")
        self.show_health()

    def computer_turn(self):
        """Ход компьютера."""
        print("Ход компьютера!")
        self.computer.attack(self.player)
        self.show_health()

    def show_health(self):
        """Выводит текущее здоровье героев."""
        print(f"{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")

if __name__ == "__main__":
    game = Game()
    game.start()
