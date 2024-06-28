answer = 1
for _ in range(3):
    answer *= int(input())
answer = str(answer)
for x in range(0, 10):
    print(answer.count(str(x)))