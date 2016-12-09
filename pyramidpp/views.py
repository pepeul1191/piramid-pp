from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='myroute')
def myview(request):
    return Response('OK')

@view_config(route_name='idea')
def site_view(request):
    return Response(request.matchdict['id'])

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'PyramidPP'}
