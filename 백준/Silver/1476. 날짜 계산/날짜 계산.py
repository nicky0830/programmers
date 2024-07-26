E, S, M = map(int, input().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0

start = 0
while True:
    S_num = 28 * start  + S
    if S_num > 0 and S_num % 19 == M and S_num %15 == E:
        print(S_num)
        break
    start += 1