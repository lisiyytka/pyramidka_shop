from pyramid.view import view_config
from pyramid.response import Response

from pyramidka_shop.models.bin import *

from sqlalchemy.exc import DBAPIError

from .. import models

users_bin = dict()


@view_config(route_name='home', renderer='../templates/main.jinja2')
def my_view(request):
    user_bin = None
    if request.params.__contains__('add') or request.params.__contains__('remove'):
        if not users_bin.__contains__('0'):
            users_bin['0'] = Bin(0)

        user_bin = users_bin['0']
        if request.params.__contains__('add'):
            user_bin.add(request.params['add'])
        elif request.params.__contains__('remove'):
            user_bin.remove(request.params['remove'])

    try:
        products = request.dbsession.query(models.Product).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return {'products': products,
            'project': 'pyramidka_shop',
            'bin': user_bin}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
