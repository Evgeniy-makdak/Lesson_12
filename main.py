from logistics import *
import json

with open('items.json', 'r', encoding='utf-8') as file:
    item_list = json.load(file)
it = item_list[0]


def main():
    store = Store(it)
    shop = Shop({})
    while True:
        print(f'На складе находится следующая продукция: {store.get_items()}')
        print(f'Свободных мест на складе: {store.get_free_space()}')
        print(f'Уникальных продуктов на складе: {store.get_unique_items_count()}')
        print(f'В магазине хранится {shop.get_items()}')

        from_1 = "store"
        to = "shop"

        product = input("Введите наименование продукции для перемещения: ")
        amount = int(input("Введите количество товара: "))

        print(f"Курьер забирает {amount} {product} из {from_1} и отвозит в {to}")
        request = Request(from_1, to, amount, product)
        store.remove(count=request.amount, product_name=request.product)
        shop.get_free_space()
        shop.add(count=request.amount, product_name=request.product)
        print(f'На складе хранится {store.get_items()}')
        # print(f'В магазине хранится {shop.get_items()}')


main()
