n, m, d = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) + (m + 1) * (d - 1) >= n:
    print('YES')
    ans = []
    m = n - sum(a)
    for i, c in enumerate(a):
        r = min(m, d - 1)
        ans.extend([i + 1] * c + [0] * r)
        m -= r
    ans = [0] * m + ans
    print(*ans)
else:
    print('NO')