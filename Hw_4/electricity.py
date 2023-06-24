def greedy(n, s):
    n1 = (n + 1) // 2
    ls = []
    rs = []
    for i in range(n):
        key, value = list(map(int, input().split(" ")))
        ls.append(key)
        rs.append(value)
    for l_ in ls:
        s -= l_
    lbs, rbs = 1, 1000000001
    while lbs + 1 < rbs:
        m = (lbs + rbs) // 2
        st = sorted((min(l_, m) for (l_, r) in zip(ls, rs) if r >= m), reverse=True)
        if len(st) >= n1 and m * n1 <= s + sum(st[:n1]):
            lbs = m
        else:
            rbs = m
    return lbs


n, s = list(map(int, input().split(" ")))
print(greedy(n,s))