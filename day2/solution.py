from helper import check_adjacent_values_safety, remove_single_bad_level

with open("day2.txt", "r") as f:
    safe_count = 0  # this will keep count of how many safe report are there
    # get each line in txt file
    for row in f:
        report = row.strip().split()
        state = {
            "levels": None
        }  # Using dict to maintain state # Either report is increasing or decreasing
        is_safe = True  # a flag wether a report is safe or unsafe

        for i in range(len(report) - 1):
            if not check_adjacent_values_safety(report, i, state):
                if remove_single_bad_level(report):
                    # what keyword should be in here
                    continue
                is_safe = False
                break

        if is_safe:
            safe_count += 1


print(safe_count)
