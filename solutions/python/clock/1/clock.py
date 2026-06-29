class Clock:
    def __init__(self, hour, minute):
        # Calculate total minutes and normalize
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self):
        # Return valid Python code to recreate the object
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        # Return human-readable time in HH:MM format
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        # Two clocks are equal if they represent the same time
        if not isinstance(other, Clock):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        # Add minutes and return a new Clock
        total_minutes = self.hour * 60 + self.minute + minutes
        return Clock(0, total_minutes)

    def __sub__(self, minutes):
        # Subtract minutes and return a new Clock
        total_minutes = self.hour * 60 + self.minute - minutes
        return Clock(0, total_minutes)