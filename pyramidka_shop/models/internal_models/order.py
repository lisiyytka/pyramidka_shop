from pyramidka_shop.all_products.all_products import *


class Order(object):
    def __init__(self, order_id: str, name: str, phone: str, tea_list: list):
        self.id = order_id
        self.name = name
        self.phone = phone
        self.tea_list = tea_list
        self.price = compute_price(self.tea_list)


def compute_price(tea_list: list) -> int:
    summa = 0
    for tea in tea_list:
        all_products = ProductInitializer()
        price = all_products.products[tea].price
        summa = summa + price
    return summa

