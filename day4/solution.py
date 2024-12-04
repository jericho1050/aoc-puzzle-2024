from helper import *

with open("day4.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]
    max_length = max(len(line) for line in lines)
    arr_characters = [list(line.ljust(max_length)) for line in lines]

xmas_count = 0
xmas_count += horizontal_search(arr_characters)
xmas_count += vertical_search(arr_characters)
xmas_count += diagonal_search(arr_characters)
print(xmas_count)
