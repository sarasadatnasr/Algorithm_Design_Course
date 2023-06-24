class fenwick(object):
    def __init__(self, n):
        self.n = n
        self.cul = [0] * n
        self.maxd = len(bin(n)) - 3
    def update(self, index, diff):
        i = index
        while i < self.n:
            self.cul[i] += diff
            i += (i + 1) & (-i - 1)
    def getaccu(self, index):
        output = 0
        i = index
        while i >= 0:
            output += self.cul[i]
            i -= (i + 1) & (-i - 1)
        return output


def main(t):
    n = int(input())
    s = input()
    curr = 0
    stack = []
    accuneg = 0
    ans = 0
    mincurr = 0
    maxcurr = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '(':
            curr += 1
            if len(stack) > 0:  accuneg -= stack.pop()
        else:
            curr -= 1
            stack.append(n - i)
            accuneg += stack[-1]
        ans += accuneg
        mincurr = min(mincurr, curr)
        maxcurr = max(maxcurr, curr)
    fcount = fenwick(maxcurr - mincurr + 1)
    faccu = fenwick(maxcurr - mincurr + 1)
    fcount.update(-mincurr, 1)
    faccu.update(-mincurr, -mincurr)
    curr = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '(':
            curr += 1
        else:
            curr -= 1
        fcount.update(curr - mincurr, 1)
        faccu.update(curr - mincurr, curr - mincurr)
        ans += fcount.getaccu(curr - mincurr) * (curr - mincurr) - faccu.getaccu(curr - mincurr)
    return ans

result = []
T = int(input())
t = 1
while t <= T:
    result.append(main(t))
    t += 1
for i in range(len(result)):
    print(result[i])