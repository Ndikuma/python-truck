class BowlingGame:
    def __init__(self):
        self._rolls = []
        self._current_frame_rolls = []
        self._frame_count = 1

    def roll(self, pins):
        # 1. Basic Pin Validation
        if not (0 <= pins <= 10):
            raise ValueError("Pins must have a value from 0 to 10")
            
        # 2. Check if the game is already over
        if self._frame_count > 10:
            raise IndexError("Cannot roll after game is over")

        # 3. Handle validation for frames 1 through 9
        if self._frame_count < 10:
            if len(self._current_frame_rolls) == 0:
                if pins == 10:  # Strike!
                    self._rolls.append(pins)
                    self._frame_count += 1
                else:
                    self._current_frame_rolls.append(pins)
                    self._rolls.append(pins)
            else:
                if self._current_frame_rolls[0] + pins > 10:
                    raise ValueError("Pin count exceeds pins on the lane")
                self._rolls.append(pins)
                self._current_frame_rolls = []
                self._frame_count += 1
                
        # 4. Handle validation for the tricky 10th frame
        else:
            self._current_frame_rolls.append(pins)
            # Two rolls down in the 10th frame
            if len(self._current_frame_rolls) == 2:
                # If first roll wasn't a strike, and together they exceed 10 (invalid spare)
                if self._current_frame_rolls[0] != 10 and sum(self._current_frame_rolls) > 10:
                    raise ValueError("Pin count exceeds pins on the lane")
                # If it's an open frame (less than 10 pins), the game ends right here
                if sum(self._current_frame_rolls) < 10:
                    self._rolls.append(pins)
                    self._frame_count += 1
                    return
            # Three rolls down (Fill ball reached)
            elif len(self._current_frame_rolls) == 3:
                # If the first two were strikes, the third cannot exceed 10 pins
                if self._current_frame_rolls[0] == 10 and self._current_frame_rolls[1] != 10:
                    if self._current_frame_rolls[1] + pins > 10:
                        raise ValueError("Pin count exceeds pins on the lane")
                self._rolls.append(pins)
                self._frame_count += 1
                return

            self._rolls.append(pins)

    def score(self):
        # Check if the game is incomplete
        if self._frame_count <= 10:
            raise IndexError("Score cannot be calculated until the game is over")
            
        total_score = 0
        roll_idx = 0
        
        # Calculate scores across 10 frames sequentially
        for _ in range(10):
            # Case 1: Strike
            if self._rolls[roll_idx] == 10:
                total_score += 10 + self._rolls[roll_idx + 1] + self._rolls[roll_idx + 2]
                roll_idx += 1
            # Case 2: Spare
            elif self._rolls[roll_idx] + self._rolls[roll_idx + 1] == 10:
                total_score += 10 + self._rolls[roll_idx + 2]
                roll_idx += 2
            # Case 3: Open Frame
            else:
                total_score += self._rolls[roll_idx] + self._rolls[roll_idx + 1]
                roll_idx += 2
                
        return total_score