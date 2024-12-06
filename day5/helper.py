from typing import Union, Tuple


# Reference: https://stackoverflow.com/questions/38130895/find-middle-of-a-list for find middle lol
# code from: @Kyle Baker
def findMiddle(input_list) -> Union[int, Tuple[int, int]]:
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return input_list[int(middle - 0.5)]
    else:
        return (input_list[int(middle)], input_list[int(middle - 1)])
