t = int(input())


for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))


    max_numbness = 0


    for i in range(n):

        current_xor = 0

        for j in range(i, n):

            current_xor ^= a[j]

            current_numbness = max(a[i:j+1]) ^ current_xor

            max_numbness = max(max_numbness, current_numbness)


    print(max_numbness)