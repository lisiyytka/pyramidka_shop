from pyramidka_shop.models.bin import Bin

users_bin = dict()


def register_product(request) -> Bin:
    if not users_bin.__contains__('0'):
        users_bin['0'] = Bin(0)

    user_bin = users_bin['0']
    if request.params.__contains__('add'):
        user_bin.add(request.params['add'])
    elif request.params.__contains__('remove'):
        user_bin.remove(request.params['remove'])

    return user_bin
