"""

Fixtures are methods in Pytest that provide a fixed baseline for tests to
run on top of.

A fixture can be used to set up preconditions for a test, provide data,
or perform a teardown after a test is finished.

"""

from decimal import Decimal

from app.package_01.script_02 import TemperatureConverter

import pytest


@pytest.fixture
def sensor():
    obj: TemperatureConverter = TemperatureConverter()
    yield obj
    del obj


def test_app__farenheit(sensor: TemperatureConverter):
    assert sensor.farenheit(Decimal('32.5')) == Decimal('90.5')
    assert sensor.farenheit(Decimal('25')) == Decimal('77')
    assert sensor.farenheit(Decimal('18')) == Decimal('64.4')
    assert sensor.farenheit(Decimal('12')) == Decimal('53.6')
    assert sensor.farenheit(Decimal(8)) == Decimal('46.4')


def test_app__celcius(sensor: TemperatureConverter):
    assert sensor.celsius(Decimal('90')) == Decimal('32.222')
    assert sensor.celsius(Decimal('77')) == Decimal('25')
    assert sensor.celsius(Decimal('64.4')) == Decimal('18')
    assert sensor.celsius(Decimal('53.6')) == Decimal('12')
    assert sensor.celsius(Decimal('46.4')) == Decimal('8')
