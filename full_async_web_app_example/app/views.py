# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp.web import json_response


class Index(web.View):
    async def get(self):
        return json_response({'error': None, 'message': 'hello'})
