n = int(input())
answer = []
for i in range(2, n+1):
    while n % i == 0:
        answer.append(i)
        n = n//i
answer.sort()
for a in answer:
    print(a)