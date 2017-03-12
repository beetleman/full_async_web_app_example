import pytest
import os
from playhouse.db_url import connect
from peewee_migrate import Router

from full_async_web_app_example.app import create as create_app
from full_async_web_app_example.app.config import Test

TEST_ROOT = os.path.abspath(
    os.path.dirname(__name__)
)


@pytest.fixture
def conf():
    return Test


@pytest.fixture
def app(loop, conf):
    return create_app(loop, conf=conf)


@pytest.fixture
def migrations(app, conf):
    database = connect(conf.database_url)
    migrate_dir = os.path.join(os.path.dirname(TEST_ROOT), 'migrations')
    router = Router(database, migrate_dir=migrate_dir)
    router.run()


@pytest.fixture
def cli(app, loop, test_client):
    return loop.run_until_complete(test_client(app))
