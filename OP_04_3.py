def bank(a, years):
    interest_rate = 0.10  # 10%
    total_amount = a
    for year in range(years):
        total_amount += total_amount * interest_rate
    return total_amount
# Пример использования функции
initial_investment = 10000  # сумма вклада в рублях
investment_years = 5       # срок в годах
final_amount = bank(initial_investment, investment_years)
print(f"Сумма на счету через {investment_years} лет составит: {final_amount:.2f} рублей")
print()
### Объяснение:
# - Функция `bank` принимает два аргумента: `a` (сумма вклада) и `years` (количество лет).
# - Мы устанавливаем процентную ставку на уровне 10% (0.10).
# - Используем цикл `for`, чтобы пройтись по каждому году, добавляя к общей сумме 10% от текущей суммы.
# - В конце функция возвращает общую сумму, которая будет на счету пользователя.
# Вы можете изменить значения `initial_investment` и `investment_years`,
# чтобы протестировать функцию с различными параметрами.
def bank(a, years):
    # Изначальная сумма вклада
    total = a
    # Проходим по каждому году и увеличиваем сумму на 10%
    for year in range(years):
        total += total * 0.1  # Прибавляем 10% от текущей суммы
    return total
# Пример использования функции
a = float(input("Введите сумму вклада (в рублях): "))
years = int(input("Введите срок вклада (в годах): "))
final_amount = bank(a, years)
print(f"Сумма на счету через {years} лет: {final_amount:.2f} рублей")
