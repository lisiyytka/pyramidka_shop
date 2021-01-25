from pyramid.view import view_config
from ..bin_registration.bin_registration import register_product
from ..all_products.all_products import ProductInitializer

all_products = ProductInitializer()


@view_config(route_name='home', renderer='../templates/main.jinja2')
def main_view(request):
    user_bin = None
    if request.params.__contains__('add') or request.params.__contains__('remove'):
        user_bin = register_product(request)

    if not all_products.products_initialized:
        all_products.initialize(request)

    return {'products': all_products.products.values(),
            'project': 'pyramidka_shop',
            'bin': user_bin}
