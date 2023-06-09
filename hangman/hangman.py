"""hangman.py

Implement a game of hangman using Functional Reactive Programming."""

# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    """Create a word for a new game of hangman."""

    def __init__(self, word: str, max_guesses: int = 9) -> None:
        self.remaining_guesses = max_guesses
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses = []

    def guess(self, char: str) -> str:
        """Guess another char, and return the masked word. [Note: returning the
        masked word wasn't specified, but it makes sense when using this
        interactively.]"""
        match self.get_status(), char, self.remaining_guesses:
            case 'win' | 'lose', _, _:
                raise ValueError("The game has already ended.")
            case _, char, _ if char in self.word and char not in self.guesses:
                # note: guessing a letter correctly (the first time) doesn't
                # cost a turn
                self.guesses.append(char)
                if self.word == self.get_masked_word():
                    self.status = STATUS_WIN
            case _, _, remaining if remaining > 0:
                self.remaining_guesses -= 1
            case _, _, 0:
                self.status = STATUS_LOSE

        return str(
            f'word: {self.get_masked_word()!r} '
            f'status: {self.get_status()}'
            # f' ({self.remaining_guesses} guesses left)'
        )

    def get_masked_word(self) -> str:
        """Return the word with the correctly guessed letters displayed."""
        letter_guesses = [
            guess for guess in self.guesses if len(guess) == 1
        ]
        return ''.join(
            [letter if letter in letter_guesses else '_'
             for letter in self.word]
        )

    def get_status(self) -> str:
        """Return the status of the game."""
        return self.status
