# определён класс "Account", иммитирующий банковский счет. Класс должен включать
# атрибуты для хранения идентификаторв владельца, баланс счета и методы для
# депозита (пополнения) и снятия средств ( если счет не нулевой)

class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")
        else:
            print("Сумма для пополнения должна быть больше 0.")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счёте")
        elif money > 0:
            self.balance -= money
            print(f"Вы успешно сняли {money}. Текущий баланс - {self.balance}")
        else:
            print("Сумма для снятия должна быть больше 0.")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")


# Пример использования
man = Account(id="12323132", balance=600)
man.all_balance()  # Показывает текущий баланс
man.deposit(500)  # Пополняет баланс
man.withdraw(100)  # Снимает средства