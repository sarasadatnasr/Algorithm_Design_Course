def find_num_box(x, u, arr):
    arr.sort(reverse=True)
    arr[u - 1], arr[u - 2] = arr[u - 2], arr[u - 1]
    unboxed = []

    for w, o, u in arr:
        if x >= w:
            trash = min((x // w), o)
            x -= trash * w
            unboxed.append(u)

    if x > 0:
        print("-1")
    else:
        print(len(unboxed))
        print(*unboxed)


x, n = map(int, input().split())
boxes = []
for i in range(n):
    k, q = map(int, input().split())
    boxes.append((10 ** k, q, i + 1))
find_num_box(x, n, boxes)