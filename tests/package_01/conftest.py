from app.package_01.script_09 import RegisteredUser

import pytest


@pytest.fixture(scope='session')
def user():
    user_obj = RegisteredUser()
    user_obj.register('john')
    yield user_obj
    del user_obj


@pytest.fixture(scope='session')
def guestUser(request: pytest.FixtureRequest):
    user_obj = RegisteredUser()

    def add_users():
        nonlocal user_obj
        user_obj.register('ramya')
        user_obj.register('radha')
        user_obj.register('murugan')

    def remove_users():
        nonlocal user_obj
        user_obj.register('ramya')
        user_obj.register('radha')
        user_obj.register('murugan')
        del user_obj

    request.addfinalizer(remove_users)
    add_users()
    return user_obj
