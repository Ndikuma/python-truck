import random
import string

class Robot:
    used_names = set()

    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        while True:
            name = (
                random.choice(string.ascii_uppercase) +
                random.choice(string.ascii_uppercase) +
                str(random.randint(0, 999)).zfill(3)
            )
            if name not in Robot.used_names:
                Robot.used_names.add(name)
                return name

    def reset(self):
        Robot.used_names.discard(self.name)
        old_name = self.name
    
        new_name = self._generate_name()
    
        # ensure it's actually different in reset scenario
        while new_name == old_name:
            new_name = self._generate_name()
    
        self.name = new_name