from helper import findMiddle

with open("ordering_rules.txt", "r") as f:

    ordering_rules = {}
    for row in f:
        x, y = row.strip().split("|")
        if x in ordering_rules:
            ordering_rules[x].append(int(y))
        else:
            ordering_rules[x] = []
            ordering_rules[x].append(int(y))

with open("day5.txt") as f:

    order_updates = []
    unorder_updates = []
    for row in f:
        update = row.strip().split(",")
        is_order = True
        for idx, num in enumerate(update):
            if num not in ordering_rules:
                is_order = False
                break
            for i in range(idx + 1, len(update)):
                if int(update[i]) not in ordering_rules[num]:
                    is_order = False
                    break
            if not is_order:
                break
        if is_order:
            order_updates.append(update)
        else:
            unorder_updates.append(update)

    for update in unorder_updates:
        for _ in range(len(update)):
            for i in range(len(update) - 1):
                curr, next = update[i], update[i + 1]
                if int(next) not in ordering_rules[curr]:
                    update[i], update[i + 1] = update[i + 1], update[i]

    total = 0  # Sum of all middle paged number from the correctly ordered_updates
    for update in unorder_updates:
        middle = findMiddle(update)
        if isinstance(middle, tuple):
            total += sum(int(x) for x in middle)
        else:
            total += int(middle)

print(total)
