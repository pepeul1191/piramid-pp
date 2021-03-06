#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid_handlers import action
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramidpp.libs.helper import Helper
import requests
import json

class Menu(object):
    def __init__(self, request):
        self.request = request

    @action(name='index', request_method='GET')
    def index(self):
        helper = Helper()
        helper.set('modulos', json.loads(helper.listar_modulos()))
        helper.set('menus', json.loads(helper.listar_menu("Accesos")))
        helper.set('activo', 'Accesos')
        response = render_to_response('../../templates/accesos/menu/index.html', {'helper':helper})
		 #response.content_type = 'text/plain'
        return response

    @action(name='bye', request_method='GET')
    def bye(self):
        helper = Helper()
        helper.set('modulos', json.loads(helper.listar_modulos()))
        helper.set('menus', json.loads(helper.listar_menu("Accesos")))
        helper.set('activo', 'Accesos')
        response = render_to_response('../../templates/accesos/menu/bye.html', {'helper':helper})
        return response