import random

from app.package_01.script_06 import vehicle_speed

import pytest


def test__vehicle_speed_low(monkeypatch: pytest.MonkeyPatch):

    def mock_function(*args, **kwargs):
        return 24

    monkeypatch.setattr(random, 'randrange', mock_function)
    value = vehicle_speed()
    assert value == 'lowspeed'


def test__vehicle_speed_normal(monkeypatch: pytest.MonkeyPatch):

    def mock_function(*args, **kwargs):
        return 45

    monkeypatch.setattr(random, 'randrange', mock_function)
    value = vehicle_speed()
    assert value == 'normal'


def test__vehicle_speed_overspeed(monkeypatch: pytest.MonkeyPatch):

    def mock_function(*args, **kwargs):
        return 73

    monkeypatch.setattr(random, 'randrange', mock_function)
    value = vehicle_speed()
    assert value == 'overspeed'


def test__vehicle_speed_danger(monkeypatch: pytest.MonkeyPatch):

    def mock_function(*args, **kwargs):
        return 98

    monkeypatch.setattr(random, 'randrange', mock_function)
    value = vehicle_speed()
    assert value == 'towed'
