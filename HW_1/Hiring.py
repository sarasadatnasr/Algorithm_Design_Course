def minimumDistance(arr):
    arr = sorted(arr)
    diff = 10 ** 20
    for i in range(len(arr)-1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]
    return diff


n, d = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))
res = []
for k in range(d):
    f, l = list(map(int, input().split(' ')))
    res.append(minimumDistance(array[f-1:l]))
for z in res:
    print(z)
