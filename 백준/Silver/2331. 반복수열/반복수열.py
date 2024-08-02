A, P = map(int, input().split())

DP = []
while True:
    if A in DP:
        break
    DP.append(A)
    check = 0
    for s in str(A):
        check += int(s)**P
    A = check

print(DP.index(A))
