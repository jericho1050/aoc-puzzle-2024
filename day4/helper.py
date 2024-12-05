import re

POSITION = tuple[tuple[int, int], tuple[int, int]]


def horizontal_search(arr: list[list[str]], word: str = "XMAS") -> int:
    xmas_count = 0
    reverse_word = word[::-1]
    for string in arr:
        line = "".join(string)
        xmas_count += line.count(word)
        xmas_count += line.count(reverse_word)
    return xmas_count


def vertical_search(arr: list[list[str]], word: str = "XMAS") -> int:
    xmas_count = 0
    reverse_word = word[::-1]
    for col in range(len(arr[0])):
        column_chars = [arr[row][col] for row in range(len(arr))]
        column_string = "".join(column_chars)
        xmas_count += column_string.count(word)
        xmas_count += column_string.count(reverse_word)
    return xmas_count


def diagonal_search(arr: list[list[str]], word: str = "XMAS") -> int:
    xmas_count = 0
    reverse_word = word[::-1]
    rows = len(arr)
    cols = len(arr[0])

    # Top-left to bottom-right diagonals
    for k in range(rows + cols - 1):
        diagonal_chars = []
        for i in range(rows):
            j = k - i
            if 0 <= j < cols:
                diagonal_chars.append(arr[i][j])
        diagonal_string = "".join(diagonal_chars)
        xmas_count += diagonal_string.count(word)
        xmas_count += diagonal_string.count(reverse_word)

    # Top-right to bottom-left diagonals
    for k in range(-rows + 1, cols):
        diagonal_chars = []
        for i in range(rows):
            j = i + k
            if 0 <= j < cols:
                diagonal_chars.append(arr[i][j])
        diagonal_string = "".join(diagonal_chars)
        xmas_count += diagonal_string.count(word)
        xmas_count += diagonal_string.count(reverse_word)

    return xmas_count


def x_max_search(arr: list[list[str]]) -> int:
    """
    find the neighbouring characters that forms a X 3x3 grid of MAS

    e.g.,

        MDS
        AAB
        MCS

    removing the irrelevant characters. You can visualize it like this

        M.S
        .A.
        M.S
    """

    xmas_count = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            # locate the current position of index

            if 0 < i and i < len(arr) - 1 and 0 < j and j < len(arr[0]) - 1:
                # Top-left to bottom-right diagonal positions
                topLeft = (i - 1, j - 1)
                bottomRight = (i + 1, j + 1)

                # Top-right to bottom-left diagonal positions
                topRight = (i - 1, j + 1)
                bottomLeft = (i + 1, j - 1)
                if check_diagonal(
                    arr, i, j, (topLeft, topRight), (bottomLeft, bottomRight)
                ):
                    xmas_count += 1

    return xmas_count


def check_diagonal(
    arr: list[list[str]],
    center_i: int,
    center_j: int,
    top_pos: POSITION,
    bottom_pos: POSITION,
) -> bool:
    """
    Check if positions are valid and form MAS/SAM pattern
    Return True if valid pattern found
    """
    if arr[center_i][center_j] != "A":
        return False

    topLeft, topRight = top_pos
    bottomLeft, bottomRight = bottom_pos

    if (
        arr[topLeft[0]][topLeft[1]] == "M"
        and arr[bottomRight[0]][bottomRight[1]] == "S"
        or arr[topLeft[0]][topLeft[1]] == "S"
        and arr[bottomRight[0]][bottomRight[1]] == "M"
    ) and (
        arr[topRight[0]][topRight[1]] == "M"
        and arr[bottomLeft[0]][bottomLeft[1]] == "S"
        or arr[topRight[0]][topRight[1]] == "S"
        and arr[bottomLeft[0]][bottomLeft[1]] == "M"
    ):
        return True
    else:
        return False
