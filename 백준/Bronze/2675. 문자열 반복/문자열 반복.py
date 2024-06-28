n = int(input())
for _ in range(n):
    num, word = input().split()
    answer = ''
    for w in word:
        answer += w * int(num)
    print(answer)