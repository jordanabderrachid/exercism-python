class SpaceAge:

    mapping = {
        "earth": 1,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.age_in_seconds = seconds

    def __on_earth_full_precision(self):
        return self.age_in_seconds / 31557600

    def __round(self, n):
        return round(n, 2)

    def __on_planet(self, planet):
        return self.__round(self.__on_earth_full_precision() / self.mapping[planet])

    def on_earth(self):
        return self.__on_planet("earth")

    def on_mercury(self):
        return self.__on_planet("mercury")
    
    def on_venus(self):
        return self.__on_planet("venus")
    
    def on_mars(self):
        return self.__on_planet("mars")
    
    def on_jupiter(self):
        return self.__on_planet("jupiter")
    
    def on_saturn(self):
        return self.__on_planet("saturn")
    
    def on_uranus(self):
        return self.__on_planet("uranus")
    
    def on_neptune(self):
        return self.__on_planet("neptune")