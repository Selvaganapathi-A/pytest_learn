import sys

import pytest


@pytest.mark.skip(reason='run this test on linux only.')
def test__linux_prepare_homefolder():
    pass


@pytest.mark.skipif(condition=sys.platform != 'linux',
                    reason='run this test on linux only.')
def test__linux_prepare_install():
    pass


@pytest.mark.xfail(raises=ZeroDivisionError)
def test__zero_division_error():
    a = 1 / 0
    assert a == float('inf')


@pytest.mark.core
def test__core_module():
    pass


@pytest.mark.util
@pytest.mark.smoke
def test__util_app():
    pass


@pytest.mark.smoke
def test__smoke_():
    pass


'''
pytest -v -s -m "not smoke and core"
pytest -v -s -m "smoke or core"
'''