def find_min_stalls(board, cow, stalls):
    gaps = []
    stalls = sorted(stalls)
    for i in range(1, cow):
        gaps.append(stalls[i] - stalls[i-1] - 1)
    gaps.sort(reverse=True)
    total = stalls[-1] - stalls[0] + 1
    for i in range(min(board - 1, cow - 1)):
        total -= gaps[i]
    return total


# main
m, s, c = map(int, input().split())
arr = []
for i in range(c):
    arr.append(int(input()))
print(find_min_stalls(m, c, arr))