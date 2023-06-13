"""raindrops.py

Solve the classic FizzBuzz problem with an extra divisor."""

NUMBER_SOUNDS = {
    # intentionally added in arbitrary order to ensure it doesn't affect
    # correctness of the code
    7: 'Plong',
    3: 'Pling',
    5: 'Plang',
}

def _is_divisible_by(dividend: int, divisor: int) -> bool:
    """Return True if dividend is evenly divisible by divisor."""
    return dividend % divisor == 0

def convert(number: int) -> str:
    """Return concatenated sounds of number divisible by the keys of
    NUMBER_SOUNDS or the number itself if it isn't evenly divisible by any of
    the aforementioned keys."""
    sounds = [NUMBER_SOUNDS[key]
              for key in sorted(NUMBER_SOUNDS.keys())
              if _is_divisible_by(number, key)]
    return ''.join(sounds) if sounds else f'{number}'
