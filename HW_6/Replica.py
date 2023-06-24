from typing import List

N = 100000
g = [[] for _ in range(N)]
vis = [False] * N
c = [0] * N

def dfs(u: int, min_c: List[int], sum_c: List[int]) -> None:
    vis[u] = True
    min_c[0] = min(min_c[0], c[u])
    sum_c[0] += c[u]
    for v in g[u]:
        if not vis[v]:
            dfs(v, min_c, sum_c)

if __name__ == "__main__":
    n, m = map(int, input().split())

    c[1:n+1] = map(int, input().split())

    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    ans = 0
    for i in range(1, n + 1):
        if not vis[i]:
            min_c = [c[i]]
            sum_c = [0]
            dfs(i, min_c, sum_c)
            ans += min_c[0]

    print(ans)