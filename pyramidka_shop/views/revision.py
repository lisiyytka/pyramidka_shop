from pyramid.view import view_config


@view_config(route_name='review', renderer='../templates/review.jinja2')
def get_orders(request):
    from .. import models
    query = request.dbsession.query(models.Order)
    info = query.all()
    return {'info': info}
