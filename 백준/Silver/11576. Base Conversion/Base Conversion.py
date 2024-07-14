a, b = map(int, input().split())
n = int(input())
x = input().split()
tens  = 0 
answer = []
for i, e in enumerate(x[::-1]):
    tens += int(e) * a ** i

while tens > 0:
    answer.append(str(tens % b))
    tens = tens // b

print(' '.join(answer[::-1]))