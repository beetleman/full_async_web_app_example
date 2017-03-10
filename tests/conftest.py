import pytest

from full_async_web_app_example.app import create as create_app
from full_async_web_app_example.app.config import Test


@pytest.fixture
def app(loop):
    return create_app(loop, conf=Test)


@pytest.fixture
def cli(app, loop, test_client):
    return loop.run_until_complete(test_client(app))
