from pyramid.view import view_config


@view_config(route_name='offices', renderer='../templates/offices.jinja2')
def get_orders(request):
    from .. import models
    query = request.dbsession.query(models.Office)
    info = query.all()
    handled_info = []
    for data in info:
        handled_info.append(models.OfficeHandler(data))
    return {'info': handled_info}
