import pytest


def test_math():
    assert 1 + 2 == 3
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0 == float('inf')


def test_text():
    assert "Googol is 100 zeros.".lower() == 'googol is 100 zeros.'
    assert "Googol is 100 zeros.".title() == 'Googol Is 100 Zeros.'
    assert "Googol is 100 zeros.".upper() == 'GOOGOL IS 100 ZEROS.'
    assert "Googol is 100 zeros.".capitalize() == 'Googol is 100 zeros.'
    assert "Googol is 100 zeros.".find("100") == 10


def test_text_2():
    text = 'Bard is waste'
    assert text.partition('is') == ('Bard ', 'is', ' waste')


"""
How To Filter Tests Effortlessly With Pytest -K Options
https://pytest-with-eric.com/introduction/pytest-k-options/

only run tests that are text related 'text'
pytest -k text


can also use `not, and, or ` keywords in test options.
only run tests that are text related 'text' only
pytest -k "not math and text"


run a single test from tests
pytest -v tests/package_01/test_script_01.py::test_text_2
"""
