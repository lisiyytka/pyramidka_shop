import transaction

from pyramidka_shop.models.bin import Bin
from pyramidka_shop.models.internal_models.order import compute_price
from pyramidka_shop.models.order import Order


def create_order(request, user_bin: Bin):
    order = Order(
        name=request.params['name'],
        phone=request.params['phone'],
        tea_list=str(user_bin.products),
        price=compute_price(user_bin.products)
    )
    request.dbsession.add(order)
    transaction.commit()

    query = request.dbsession.query(Order)
    return query.order_by(Order.id.desc()).first()
