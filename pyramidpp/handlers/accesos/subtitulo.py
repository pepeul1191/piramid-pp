#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid_handlers import action
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramidpp.libs.helper import Helper
import requests
import json

class Subtitulo(object):
    def __init__(self, request):
        self.request = request

    @action(name='listar', request_method='GET')
    def listar(self):
        helper = Helper()
        url = helper.get('accesos') + "modulo/listar"
        response = requests.get(url)
        return Response(response.text)