n = input()
answer = []
for i in range(len(n)):
    answer.append(n[i:])
answer.sort()
for a in answer:
    print(a)