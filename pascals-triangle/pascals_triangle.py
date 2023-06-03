from typing import List


def generate_next_row(prev_row: List[int]) -> List[int]:
    next_row = [1 for _ in range(len(prev_row) + 1)]
    for i, _ in enumerate(next_row):
        if 0 < i and i < len(next_row) - 1:
            next_row[i] = prev_row[i-1] + prev_row[i]
        else:
            pass
    return next_row


def rows_helper(rows_remaining: int, acc: List[List[int]]) -> List[List[int]]:
    if rows_remaining == 0:
        return acc
    else:
        rows_helper(
            rows_remaining - 1,
            # >>> [[1]] + [generate_next_row([[1]][-1])]
            # [[1], [1, 1]]
            acc + [generate_next_row(acc[-1])]
        )


def rows(row_count: int) -> List[List[int]]:
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    else:
        return rows_helper(row_count, [[1]])
