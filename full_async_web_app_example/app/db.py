from peewee import Proxy, Model
import peewee_async
from playhouse.db_url import parse

from .config import get_config


database_proxy = Proxy()  # Create a proxy for our db.


class BaseModel(Model):
    class Meta:
        database = database_proxy  # Use proxy for our DB.


def get_objects(app):
    return app['objects']


def get_database(app):
    return app['database']


def setup(app):
    conf = get_config(app)
    database = peewee_async.PooledPostgresqlDatabase(
        **parse(conf.database_url)
    )
    app['database'] = database

    objects = peewee_async.Manager(database)
    database.set_allow_sync(False)
    app['objects'] = objects

    database_proxy.initialize(database)
