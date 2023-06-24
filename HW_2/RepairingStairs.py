cache = {}

#
def Builder(n):
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res


def counter(n, k):
    if k == 0:
        return 0
    if k == 1:
        return Builder(n) & 1
    if k % 2 == 1:
        t = counter(n, k - 1)
        x = Builder((k - 1) ^ (n + k - 1)) & 1
        return t + x
    if (n, k) in cache:
        return cache[(n, k)]
    if n % 2 == 0:
        one_cell = 2
        zero_cell = 0
        cnt1 = counter(n // 2, k // 2)
        cnt0 = k // 2 - cnt1
    else:
        one_cell = 0
        zero_cell = 1
        cnt1 = counter(n // 2, k // 2) + counter(n // 2 + 1, k // 2)
        cnt0 = k - cnt1
    res = one_cell * cnt1 + zero_cell * cnt0
    cache[(n, k)] = res
    return res


# Main
res = []
t = int(input())

for z in range(0, t):
    n, m = list(map(int, input().split(' ')))
    res.append(counter(n, m))

for j in res:
    print(j)

''' 
6
1 1
5 10
34 211
73 34
19124639 56348772
12073412269 96221437021
'''