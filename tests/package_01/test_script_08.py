import os

import pytest


def test__grant_user_access_1(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv('aws-service', 'lambda')
    assert 'aws-service' in os.environ and os.environ['aws-service'] == 'lambda'
    monkeypatch.delenv('aws-service')
