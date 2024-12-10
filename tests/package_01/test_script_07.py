from app.package_01.script_07 import grant_user_access, USER

import pytest


def test__grant_user_access_1(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setitem(USER, 'service', 'aws-secure')
    assert grant_user_access('Tesla') is True
    monkeypatch.delitem(USER, 'service')


def test__grant_user_access_2(monkeypatch: pytest.MonkeyPatch):
    assert grant_user_access('Pandas') is False
    monkeypatch.setitem(USER, 'name', 'Tesla')
    assert USER['name'] == 'Tesla'
    assert USER['access-code'] == '404'
    monkeypatch.delitem(USER, 'access-code')
    monkeypatch.delitem(USER, 'name')
