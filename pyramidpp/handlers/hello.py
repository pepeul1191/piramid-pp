#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid_handlers import action
from pyramid.response import Response

class Hello(object):
    def __init__(self, request):
        self.request = request

    @action(name='index', request_method='GET')
    def index(self):
        return Response('Hello world!')

    @action(name='bye', request_method='GET')
    def bye(self):
        return Response('bye')