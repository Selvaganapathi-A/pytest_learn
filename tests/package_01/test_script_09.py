from app.package_01.script_09 import RegisteredUser

import pytest


def test__register_new_user(user: RegisteredUser):
    assert user.register('madhan') == 2
    assert user.register('mukesh') == 3


def test__check_user_is_regisered(user: RegisteredUser):
    assert user.check_user('ramya') is False
    assert user.check_user('john') is True


def test__unregister_user(user: RegisteredUser):
    assert user.unregister('john') == 2
    assert user.unregister('mukesh') == 1
    assert user.unregister('madhan') == 0
    with pytest.raises(ValueError):
        user.unregister('ramya')


def test__register_new_user_1(guestUser: RegisteredUser):
    assert guestUser.register('guru') == 4
    assert guestUser.register('mukunth') == 5


def test__check_user_is_regisered_1(guestUser: RegisteredUser):
    assert guestUser.check_user('ramya') is True
    assert guestUser.check_user('john') is False


def test__unregister_user_1(guestUser: RegisteredUser):
    assert guestUser.unregister('ramya') == 4
    assert guestUser.unregister('guru') == 3
    with pytest.raises(ValueError):
        guestUser.unregister('meera')
