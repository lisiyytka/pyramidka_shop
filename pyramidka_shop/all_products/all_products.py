from pyramidka_shop import models
from pyramidka_shop.models.internal_models.product import Product
from sqlalchemy.exc import DBAPIError
from pyramid.response import Response


class ProductInitializer(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProductInitializer, cls).__new__(cls)
            cls.instance.products = dict()
            cls.instance.products_initialized = False
        return cls.instance

    def initialize(self, request):
        try:
            prods = request.dbsession.query(models.Product).all()
        except DBAPIError:
            return Response("", content_type='text/plain', status=500)

        for product in prods:
            self.products[product.name] = Product(product.name, product.price, product.adr)
        self.products_initialized = True
