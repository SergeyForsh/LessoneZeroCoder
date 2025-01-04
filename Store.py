# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес,
# название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
# Методы: добавить товар, удалить товар извлечь цену по названию ( если нет товара, то None),
# обновлять цену

class Store:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}'удалён из ассортимента.")

        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")


store1 = Store("Shampoo for All", "Riga, Brivibas iela 46",
               {"Her hear": 4.50,
                "His hear": 2.80,
                "Baby hear": 2.90})
store2 = Store("Shampoo and You", "Riga, Stabu iela 113",
               {"Her hear": 4.20,
                "His hear": 2.50,
                "Baby hear": 2.70})
store3 = Store("All about your hear", "Riga, Kleisti iela 110",
               {"Her hear": 5.05,
                "His hear": 3.00,
                "Baby hear": 3.05})
store4 = Store("Coner Shop", "Riga, Avotu  iela 2",
               {"Her hear": 3.70,
                "His hear": 2.20,
                "Baby hear": 2.90})

for Store in [store1, store2, store3, store4]:
    print(f"Shop:{Store.name}")
    print(f"address:{Store.address}")
    print("Nomenclature:")
    for item, price in Store.items.items():
        print(f"  - {item}: {price} eur.")
        print()





