# Globals for the directions
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

class Robot:
    # Clockwise order of directions
    _DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self._turn_right()
            elif instruction == 'L':
                self._turn_left()
            elif instruction == 'A':
                self._advance()
            else:
                raise ValueError(f"Invalid instruction: {instruction}")

    def _turn_right(self):
        # Move forward 1 step in the clockwise list
        current_idx = self._DIRECTIONS.index(self.direction)
        self.direction = self._DIRECTIONS[(current_idx + 1) % 4]

    def _turn_left(self):
        # Move backward 1 step in the clockwise list
        current_idx = self._DIRECTIONS.index(self.direction)
        self.direction = self._DIRECTIONS[(current_idx - 1) % 4]

    def _advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        elif self.direction == WEST:
            self.coordinates = (x - 1, y)