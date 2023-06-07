"""hangman.py

Implement a game of hangman using Functional Reactive Programming."""

from typing import List, TypeVar, Sequence


T = TypeVar('T')

# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


def _get_all_indices(obj: T, seq: Sequence) -> List[int]:
    """Get the indices of all elements in seq equal to obj."""
    # stolen from https://stackoverflow.com/a/28182579/2677392
    return [index for index, value in enumerate(seq) if value == obj]


def _replace_at_indices(
        xs: List[T], replacement: T, indices: List[int]) -> List[T]:
    """Replace the elements of xs with replacement at the given indices."""
    for index in indices:
        xs[index] = replacement
    return xs


class Hangman:
    """Create a word for a new game of hangman."""
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses = []

    def guess(self, char):
        """Guess another letter."""
        if self.get_status() == STATUS_ONGOING and\
           self.remaining_guesses >= 0:
            if char in self.word and char not in self.guesses:
                self.guesses.append(char)
                if self.get_masked_word() == self.word:
                    self.status = STATUS_WIN
            elif self.remaining_guesses == 0:
                self.status = STATUS_LOSE
            else:
                self.remaining_guesses -= 1
        else:
            raise ValueError("The game has already ended.")

    def get_masked_word(self):
        """Return the word with the correctly guessed letters displayed."""
        masked_list = ['_' for letter in self.word]
        # only unmask single letter replacements
        for letter in [guess for guess in self.guesses if len(guess) == 1]:
            _replace_at_indices(
                masked_list, letter, _get_all_indices(letter, self.word))
        masked_word = ''.join(masked_list)
        return masked_word

    def get_status(self):
        """Return the status of the game."""
        return self.status
