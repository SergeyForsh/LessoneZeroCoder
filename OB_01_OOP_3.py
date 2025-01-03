class Store:
    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым ассортиментом."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина.

        Args:
            item_name (str): Название товара.
            price (float): Цена товара.
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина, если он существует.

        Args:
            item_name (str): Название товара для удаления.
        """
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию.

        Args:
            item_name (str): Название товара.

        Returns:
            float: Цена товара или None, если товар отсутствует.
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновляет цену существующего товара.

        Args:
            item_name (str): Название товара.
            new_price (float): Новая цена товара.
        """
        if item_name in self.items:
            self.items[item_name] = new_price

# Пример использования:
store = Store("My Store", "123 Market St")
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)
print(store.items)  # {'apples': 0.5, 'bananas': 0.75}

store.update_price("apples", 0.6)
print(store.get_price("apples"))  # 0.6

store.remove_item("bananas")
print(store.items)  # {'apples': 0.6}

### Объяснение исправлений:
# 1. ** Метод
# `__init__` **: Исправлено
# название метода инициализации на `__init__`. Это позволяет правильно инициализировать объект
# класса `Store`. Теперь код корректно создаёт объект магазина, добавляет товары, обновляет их цены
# и удаляет товары из ассортимента. Вы можете запустить код, и он должен работать без ошибок.