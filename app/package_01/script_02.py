from decimal import Decimal


class TemperatureConverter:

    def farenheit(self, degree: Decimal) -> Decimal:
        value: Decimal = ((degree * 9) / 5) + 32
        return value.quantize(Decimal('1.000'))

    def celsius(self, farenheight: Decimal) -> Decimal:
        value: Decimal = ((farenheight - 32) * 5) / 9
        return value.quantize(Decimal('1.000'))
