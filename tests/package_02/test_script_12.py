import os
import pytest

type DICT = dict[str, str]


@pytest.mark.usefixtures("apple", "potato", "temp_folder")
def test__edible(apple: DICT, potato: DICT):
    assert apple == {"Fruit": "apple"}
    assert potato == {"Veggie": "Potato"}
    assert os.listdir() == list()
