def min_jump_distance(t, test_cases):
    results = []
    for case in test_cases:
        n = len(case)
        max_gap = 0
        current_gap = 0
        for i in range(n):
            if case[i] == 'L':
                current_gap += 1
            else:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
        max_gap = max(max_gap, current_gap)
        results.append(max_gap + 1)
    return results


test_cases = []
t = int(input())
for i in range(t):
    test_cases.append(input())

result = min_jump_distance(t, test_cases)
for i in range(t):
    print(result[i])
