class Bin(object):
    def __init__(self, owner_id):
        self.owner_id = owner_id
        self.products = list()

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)
