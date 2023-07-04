from datetime import date, timedelta


class Popsicles:
    def __init__(self, price, flavor, color, expiration_date, popularity):
        self._price = price
        self._flavor = flavor
        self._color = color
        self._expiration_date = expiration_date
        self._popularity = popularity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self._expiration_date = expiration_date

    @property
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        self._popularity = popularity

    def set_expiration_date(self):
        current_date = date.today()
        expiration_date = current_date + timedelta(days=14)
        self.set_expiration_date(expiration_date)
