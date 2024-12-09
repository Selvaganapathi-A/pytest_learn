from app.package_01.script_03 import app
from fastapi.testclient import TestClient

import orjson
import pytest


@pytest.fixture
def server():
    server: TestClient = TestClient(app)
    yield server
    del server


@pytest.fixture
def header():
    return {
        "Content-Type": 'application/json',
    }


def test_api__homepage(server: TestClient, header: dict[str, str]):
    response = server.get('/', headers=header)
    assert orjson.loads(response.content) == {'about': 'convert temperature'}


def test_api__to_farenheight(server: TestClient, header: dict[str, str]):
    response = server.get('/farenheight/30', headers=header)
    assert orjson.loads(response.content) == {'farenheight': 86.0}


def test_api__to_celcius(server: TestClient, header: dict[str, str]):
    response = server.get('/celsius/104', headers=header)
    assert orjson.loads(response.content) == {'celsius': 40.0}
