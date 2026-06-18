class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600
    
    PLANETS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds
    
    def _age_on_planet(self, orbital_period):
        earth_years = self.seconds / self.EARTH_YEAR_SECONDS
        return round(earth_years / orbital_period, 2)
    
    def __getattr__(self, name):
        # Handle methods like on_mercury, on_earth, etc.
        if name.startswith('on_'):
            planet = name[3:]  # Remove 'on_' prefix
            if planet in self.PLANETS:
                return lambda: self._age_on_planet(self.PLANETS[planet])
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")