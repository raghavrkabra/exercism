"""Solution to Space Age exercise in python track."""


def _years_on_planet(year_length):
    def no_of_years(self):
        return round(self.seconds / year_length, 2)

    return no_of_years


class SpaceAge:
    """This class convert given seconds to years on different planets."""

    def __init__(self, seconds):
        self.seconds = seconds
        self._earth_year = 31557600

    on_earth = _years_on_planet(31557600)
    on_mercury = _years_on_planet(7600544)
    on_venus = _years_on_planet(19414149)
    on_mars = _years_on_planet(59354033)
    on_jupiter = _years_on_planet(374355659)
    on_saturn = _years_on_planet(929292362)
    on_uranus = _years_on_planet(2651370019)
    on_neptune = _years_on_planet(5200418560)
