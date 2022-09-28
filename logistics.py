class Storage:
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    def add(self, product_name: str, count: int):
        if product_name in self.items:
            self.items[product_name] += count
        else:
            self.items[product_name] = count

    def remove(self, product_name: str, count: int):
        if product_name in self.items and count <= self.items[product_name]:
            self.items[product_name] -= count
        elif self.items[product_name] == 0:
            self.items.pop(self.items[product_name])
            return True

    def get_free_space(self):
        free_space = self.capacity - sum(self.items.values())
        return free_space

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)

    def add(self, product_name: str, count: int):
        if count <= self.get_free_space():
            super().add(product_name, count)


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, product_name: str, count: int):
        if product_name in self.get_items() or self.get_unique_items_count() < 5:
            super().add(product_name, count)


class Request:
    def __init__(self, from_1: str, to: str, amount: int, product: str):
        self.from_1 = from_1
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f'Доставить из {self.from_1} в {self.to} {self.amount}, {self.product}'
