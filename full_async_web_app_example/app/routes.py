# -*- coding: utf-8 -*-
from .views import Index


ROUTERS = (
    ('/', Index, 'index'),
)


def setup(app):
    for path, handler, name in ROUTERS:
        resource = app.router.add_resource(path, name=name)
        resource.add_route('*', handler)
