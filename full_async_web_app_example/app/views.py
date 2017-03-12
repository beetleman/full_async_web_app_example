# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp.web import json_response
import logging


logger = logging.getLogger(__name__)


class Index(web.View):
    async def get(self):
        logger.warning(self.request.headers)
        return json_response({'error': None, 'message': 'hello'})
