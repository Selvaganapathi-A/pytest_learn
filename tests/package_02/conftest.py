import os
import tempfile

import pytest


@pytest.fixture(scope='session')
def apple() -> dict[str, str]:
    return {'Fruit': 'apple'}


@pytest.fixture(scope='session')
def potato() -> dict[str, str]:
    return {'Veggie': 'Potato'}


@pytest.fixture
def temp_folder():
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        yield
        os.chdir(cwd)
