# -*- coding: utf-8 -*-

def get_config(app):
    return app['config']


class Base:
    @classmethod
    def setup(cls, app):
        app['config'] = cls


class Main(Base):
    test = False
