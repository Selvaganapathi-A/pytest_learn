import pytest


@pytest.fixture(scope='session')
def animal(request: pytest.FixtureRequest):
    return 'aa' not in request.param


@pytest.mark.parametrize(
    'animal', ('tiger', 'lion', 'zebra', 'crocodile', 'panda', 'capybara'),
    indirect=True)
@pytest.mark.parametrize('bird', ('peacock', 'crow', 'hen', 'rooster', 'kiwi'))
def test_bird_not_in_animals(animal: str, bird: str):
    assert 'z' not in bird
    assert animal is True
