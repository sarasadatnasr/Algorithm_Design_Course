def countSubarray(arr, n, k):
    res = 0
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if summ < k:
                res += 1
    return res

n, t = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))
count = countSubarray(array, n, t)
print(count)

