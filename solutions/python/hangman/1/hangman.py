# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_chars = set()

    def guess(self, char):
        # Block further play if already finished
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        # Handle duplicate guess
        if char in self.guessed_chars:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
            return

        # New guess
        self.guessed_chars.add(char)
        
        # Wrong guess
        if char not in self.word:
            self.remaining_guesses -= 1
        
        # Check win
        if all(c in self.guessed_chars for c in self.word):
            self.status = STATUS_WIN
        # Check lose
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join([c if c in self.guessed_chars else "_" for c in self.word])

    def get_status(self):
        return self.status