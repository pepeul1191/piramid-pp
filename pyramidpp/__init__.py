from pyramid.config import Configurator
from pyramidpp.handlers.hello import Hello
from pyramidpp.handlers.error import Error
from pyramidpp.handlers.accesos.menu import Menu
from pyramidpp.handlers.accesos.modulo import Modulo
from pyramid.httpexceptions import HTTPFound
from pyramidpp.libs.helper import Helper

def notfound(request):
    #return Response('Not Found', status='404 Not Found')
    helper = Helper()
    return HTTPFound(location=helper.get("BASE_URL") + "access/error/404")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_static_view('static', 'static', cache_max_age=3600)
    ### Inicio de rutas y handlers
    config.add_route('home', '/')
    config.add_route('myroute', '/prefix/{one}/{two}')
    config.add_route('idea', 'site/{id}')
    #config.add_handler('hello_index', '/hello/index', handler=Hello, action='index')
    #config.add_handler('hello_bye', '/hello/bye', handler=Hello, action='bye')
    #get '/accesos/modulo/listar' => 'accesos/modulo#listar'
    config.add_handler('hello', '/hello/{action}', handler=Hello)
    config.add_handler('hello_index', '/hello/', handler=Hello, action='index')
    config.add_handler('menu', 'accesos/menu/{action}', handler=Menu)
    config.add_handler('modulo', 'accesos/modulo/{action}', handler=Modulo)
    ### Exceptions
    config.add_notfound_view(notfound)
    config.add_handler('get_notfound', 'access/error/404', handler=Error, action='notfound')
    ### Fin de rutas y handlers
    config.scan()
    return config.make_wsgi_app()
