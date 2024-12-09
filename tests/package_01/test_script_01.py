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