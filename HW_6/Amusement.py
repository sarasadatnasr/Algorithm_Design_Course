n, m = list(map(int, input().split()))

count = 0

while n < m:
    if m % 2 == 0:
        m //= 2
    else:
        m += 1
    count += 1

count += n - m

print(count)