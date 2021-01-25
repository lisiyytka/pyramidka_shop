from pyramid.view import view_config
from pyramidka_shop.bin_registration.bin_registration import *
from pyramidka_shop.order_creator.order_creator import create_order


@view_config(route_name='result', renderer='../templates/result.jinja2')
def order_view(request):
    user_bin = users_bin.pop('0')
    order = create_order(request, user_bin)
    return {'order': order}
