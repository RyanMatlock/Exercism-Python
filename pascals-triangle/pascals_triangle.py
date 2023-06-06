"""pascals_triangle.py

Recursively calculate Pascal's triangle to a given number of rows."""

from typing import List, Callable, TypeVar
import logging


logging.basicConfig(level=logging.WARNING)

T = TypeVar('T')


# def generate_next_row(prev_row: List[int]) -> List[int]:
#     next_row = [1 for _ in range(len(prev_row) + 1)]
#     for i, _ in enumerate(next_row):
#         if 0 < i and i < len(next_row) - 1:
#             next_row[i] = prev_row[i-1] + prev_row[i]
#         else:
#             pass
#     return next_row


def append_next_row(accumulator: List[List[int]]) -> List[List[int]]:
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

    return accumulator + [next_row]


def do_times(n: int, function: Callable[[T], T]) -> Callable[[T], T]:
    if n < 0:
        raise ValueError(f"n must be ≥ 0; given {n}.")

    while n > 0:
        return function(do_times(n - 1, function))


# def rows_helper(rows_remaining: int, acc: List[List[int]]) -> List[List[int]]:
#     if rows_remaining == 0:
#         logging.debug(f"going to return acc: {acc}")
#         return acc
#     else:
#         logging.debug(f"rows_remaining: {rows_remaining}\n"
#                       f"acc: {acc}")
#         acc.extend([generate_next_row(acc[-1])])
#         return rows_helper(
#             rows_remaining - 1,
#             # >>> [[1]] + [generate_next_row([[1]][-1])]
#             # [[1], [1, 1]]
#             # acc + [generate_next_row(acc[-1])]
#             acc
#         )

# def rows_helper(rows_remaining: int, acc: List[List[int]]) -> List[List[int]]:
#     for _ in range(rows_remaining):

def rows_helper(row_countdown: int,
                acc: List[List[int]]) -> List[List[int]]:
    if row_countdown == 0:
        return acc
    else:
        rows_helper(row_countdown - 1,
                    append_next_row(acc[-1]))


def rows(row_count: int) -> List[List[int]]:
    if row_count < 0:
        raise ValueError("number of rows is negative")
    # elif row_count == 0:
    #     return []
    # else:
    #     return rows_helper(row_count - 1, [[1]])

    # while row_count > 0:
    #     pascals_triangle.append(generate_next_row(rows(row_count - 1)))
    # that isn't right

    return rows_helper(row_count, [])
