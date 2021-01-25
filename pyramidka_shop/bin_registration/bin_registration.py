from pyramidka_shop.models.bin import Bin

users_bin = dict()


def register_product(request) -> Bin:
    if not users_bin.__contains__(request.client_addr):
        users_bin[request.client_addr] = Bin(request.client_addr)

    user_bin = users_bin[request.client_addr]
    if request.params.__contains__('add'):
        user_bin.add(request.params['add'])
    elif request.params.__contains__('remove'):
        user_bin.remove(request.params['remove'])

    return user_bin
