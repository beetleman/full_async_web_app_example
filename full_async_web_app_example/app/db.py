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
    database_proxy.initialize(database)

    app['database'] = database_proxy

    objects = peewee_async.Manager(database_proxy)
    database.set_allow_sync(False)
    app['objects'] = objects
