CHESSBOARD_MIN = 1
CHESSBOARD_MAX = 64

def square(number: int) -> int:
    """Return the number of grains on the chessboard square given by number."""
    if CHESSBOARD_MIN <= number <= CHESSBOARD_MAX:
        return 2 ** (number - 1)
    else:
        raise ValueError(
            f"square must be between {CHESSBOARD_MIN} and {CHESSBOARD_MAX}"
        )


def total() -> int:
    """Return the total number of grains on the chessboard."""
    return sum(
        [square(n) for n in range(CHESSBOARD_MIN, CHESSBOARD_MAX + 1)]
    )
