n = int(input())
e = int(n * (n - 1) / 2)
list1 = []
list2 = []
fake = []
res = ''
for i in range(e):
    x, y, f, l = input().split(' ')
    if f == '+' and l == '+':
        if not list2:
            list2.append(x)
            list2.append(y)
        else:
            if y in list2:
                list2.append(x)
            elif x in list2:
                list2.append(y)
            else:
                if x not in list1:
                    list1.append(x)
                if y not in list1:
                    list1.append(y)


if len(list1) > len(list2):
    fake = list1
else:
    fake = list2
for j in range(1, n+1):
    if str(j) in fake:
        res +='+'
    else:
        res +='-'
print(res)
