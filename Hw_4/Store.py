def greedy():
    clothes = sorted([int(i) for i in input().split()])
    shelves = 0

    # Fill shelves with two pieces of the most abundant color and one piece of the second most abundant color
    step = min(clothes[1] - clothes[0], clothes[2] - clothes[1])
    clothes[2] -= 2 * step
    clothes[1] -= step
    shelves += step

    # Scenario 1: The difference between the most abundant color and the least abundant color is less than 2
    if clothes[2] - clothes[0] < 2:
        return shelves + clothes[0]

    # Scenario 2: The number of clothes of the most abundant color is equal to the number of clothes of the second most abundant color
    if clothes[2] == clothes[1]:
        k = clothes[1] - clothes[0]
        step = k // 3 * 2
        if k % 3 > 1:
            step += 1
        return shelves + step + clothes[0]

    # Scenario 3: The number of clothes of the most abundant color is at least three times the number of clothes of the least abundant color
    if clothes[2] >= 3 * clothes[0]:
        return shelves + clothes[0] * 2

    k = clothes[2] - clothes[0]
    step = k // 3 * 2
    return shelves + step // 2 + step

print(greedy())