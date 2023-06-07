"""pascals_triangle.py

Recursively calculate Pascal's triangle to a given number of rows."""

from typing import List


def append_next_row(rows_remaining: int,
                    accumulator: List[List[int]]) -> List[List[int]]:
    """Recursively generate Pascal's triangle."""
    if rows_remaining < 0:
        raise ValueError("number of rows is negative")
    elif rows_remaining == 0:
        return accumulator
    else:
        try:
            prev_row = accumulator[-1]
            next_row = [1 for _ in range(len(prev_row) + 1)]
            for i, _ in enumerate(next_row):
                if 0 < i and i < len(next_row) - 1:
                    next_row[i] = prev_row[i-1] + prev_row[i]
                else:
                    pass
        except IndexError:
            next_row = [1]

        return append_next_row(rows_remaining - 1,
                               accumulator + [next_row])


def rows(row_count: int) -> List[List[int]]:
    """Return the first rows_count levels of Pascal's triangle."""
    return append_next_row(row_count, [])
