
def calculate_steps(n, m, p):
    bottom_steps = [1 - int(p[i]) for i in range(m)]
    top_steps = [1 - int(p[i + n]) for i in range(m)]
    num_diff_steps = sum([1 for i in range(m) if bottom_steps[i] != top_steps[i]])
    return num_diff_steps

def binary_concat(n) -> str:
    res = "0"
    while len(res) < n:
        compl = ''.join(['1' if b == '0' else '0' for b in res])
        res += compl
    return res



res = []
t = int(input())

for z in range(t):
    n, m = list(map(int, input().split(' ')))
    p = binary_concat(n + m)
    res.append(calculate_steps(n, m, p))

for x in res:
    print(x)








