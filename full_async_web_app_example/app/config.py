# -*- coding: utf-8 -*-
import os


def get_config(app):
    return app['config']


class Base:
    @classmethod
    def setup(cls, app):
        app['config'] = cls


class Main(Base):
    test = False
    database_url = os.environ.get('DATABASE_URL')


class Test(Main):
    test = True
