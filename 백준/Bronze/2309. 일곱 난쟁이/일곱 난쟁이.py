from itertools import combinations
cans = []
for _ in range(9):
    cans.append(int(input()))
cans.sort()
total = sum(cans)
for c in combinations(cans, 2):
    a,b = c
    if total - a - b == 100:
        cans.remove(a)
        cans.remove(b)
        break
for c in cans:
    print(c)