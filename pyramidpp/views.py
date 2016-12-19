from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.response import Response

@view_config(route_name='myroute')
def myview(request):
    return Response('OK')

@view_config(route_name='idea')
def site_view(request):
    return Response(request.matchdict['id'])
