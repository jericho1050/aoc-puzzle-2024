import re
from helper import multiply

# Define patterns as constants
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don't\(\)"
MUL_PATTERN = r"mul\((\d+),(\d+)\)"
COMMAND_PATTERN = f"{DO_PATTERN}|{DONT_PATTERN}|{MUL_PATTERN}"

with open("day3.txt", "r") as f:
    sum = 0
    enabled = True
    content = f.read()
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    muls = re.findall(pattern, content)
    for mul in muls:
        if re.match(DONT_PATTERN, mul):
            enabled = False
        if re.match(DO_PATTERN, mul):
            enabled = True

        matches = re.search(r"(\d+),(\d+)", mul)
        if matches and enabled:
            sum += multiply(int(matches.group(1)), int(matches.group(2)))

print(sum)
