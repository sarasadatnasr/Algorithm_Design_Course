import math
n = int(input())

n_match = int(math.log2(n - 1) + 1)
print(str(n_match) + ' ')

for column in range(n_match):
    team_1 = []
    for i in range(n):
        if i // (2 ** column) % 2 == 0:
            team_1.append(i)
    print(str(len(team_1)), end =' ')
    for player in team_1:
        print(str(player + 1), end =' ')
    print()
