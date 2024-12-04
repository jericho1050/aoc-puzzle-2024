import re


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
