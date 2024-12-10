from app.package_01.script_05 import get_todo

import pytest
import requests


class DummyResponse:

    @staticmethod
    def json() -> dict[str, int | str | bool]:
        return {
            'userId': 1,
            'id': 1,
            'title': 'delectus aut autem',
            'completed': False
        }

    @property
    def status_code(self):
        return 207


def test_todo(monkeypatch: pytest.MonkeyPatch):

    def mockrequest(*args, **kwargs) -> DummyResponse:
        return DummyResponse()

    monkeypatch.setattr(requests, "get", mockrequest)

    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = get_todo(url)
    assert response.status_code == 207
    assert response.json() == {
        'userId': 1,
        'id': 1,
        'title': 'delectus aut autem',
        'completed': False
    }
