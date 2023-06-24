n = int(input())
e = int((n * (n - 1)) / 2)
a = []
suspicious = 0
res = ''


for i in range(e):
    x, y, f, l = input().split(' ')
    if f == '+' and l == '+':
        x, y = int(x), int(y)
        exist = False
        for j in a:
            if x in j or y in j:
                j.add(x)
                j.add(y)
                exist = True
                break
        if not exist:
            a.append({x, y})


for k in a:
    if len(k) > suspicious:
        suspicious = len(k)
        fakes = k


for z in range(1, n + 1):
    if z in fakes:
        res += '+'
    else:
        res += '-'
print(res)