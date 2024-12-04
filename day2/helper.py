def check_adjacent_values_safety(report: list, i: int, state: dict) -> bool:
    """_summary_

    Args:
        report (list):The row or report
        i (int): current index
        state (dict): a mutable object , coming from the parent

    Returns:
        bool: safe or unsafe (True or False)
    """
    curr_el = int(report[i])
    next_el = int(report[i + 1])
    # if it's in range of minmax numbers then we already know it's not going to be safe
    if abs(curr_el - next_el) not in [*range(1, 4)]:
        return False
    if curr_el > next_el:
        # then we know it's not safe anymore as we're supposed to decrease
        if state["levels"] == "increasing":
            return False
        state["levels"] = "decreasing"
    if curr_el < next_el:
        # then we know it's not safe anymore as we're supposed to increase
        if state["levels"] == "decreasing":
            return False
        state["levels"] = "increasing"
    return True


def remove_single_bad_level(report: list) -> bool:
    """Try to simulate wether a report/row could be safe when removing a bad level or element

    Args:
        report (list): The row or report
        state (dict): a mutable object , coming from the parent

    Returns:
        bool: safe or unsafe (True or False)
    """

    for index in range(len(report)):
        state = {"levels": None}
        is_safe = True
        modified_report = report.copy()
        del modified_report[index]
        for i in range(len(modified_report) - 1):
            if not check_adjacent_values_safety(modified_report, i, state):
                is_safe = False
                break
        if is_safe:
            return True
    return False


if __name__ == "__main__":
    check_adjacent_values_safety()
