def calculate(section, pos):
    act = []
    pas = []
    if pos < 0:
        return 0

    for el in section:
        if ((el >> pos) & 1) == 0:
            pas.append(el)
        else:
            act.append(el)
    if len(pas) == 0:
        return calculate(act, pos - 1)
    if len(act) == 0:
        return calculate(pas, pos - 1)
    return min(calculate(pas, pos - 1),
               calculate(act, pos - 1)) + (1 << pos)


def minFinder(a, n):
    section = []
    for i in range(n):
        section.append(a[i])
    return calculate(section, 30)



n = int(input())
arr = list(map(int, input().split(' ')))
print(minFinder(arr, n))