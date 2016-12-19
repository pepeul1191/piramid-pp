#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid_handlers import action
from pyramid.response import Response
from pyramid.renderers import render_to_response

class Error(object):
    def __init__(self, request):
        self.request = request

    @action(name='notfound', request_method='GET')
    def get_notfound(self):
        response = render_to_response('../templates/error/404.html', {})
		 #response.content_type = 'text/plain'
        return response

    @action(name='notfound', request_method='POST')
    def post_notfound(self):
        return Response('bye')