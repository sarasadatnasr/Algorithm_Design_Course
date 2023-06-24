def solve():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    a = tuple(map(lambda x: int(x) - 1, input().split()))
    ans = [''] * n

    for i in range(n - 1, -1, -1):
        x = a[i]
        for u in range(n):
            for v in range(n):
                if matrix[u][v] > matrix[u][x] + matrix[x][v]:
                    matrix[u][v] = matrix[u][x] + matrix[x][v]

        upper, lower = 0, 0
        for u in a[i:]:
            for v in a[i:]:
                lower += matrix[u][v]
            if lower >= 10 ** 9:
                upper += 1
                lower -= 10 ** 9
        ans[i] = str(upper * 10 ** 9 + lower)

    print(' '.join(ans))


solve()