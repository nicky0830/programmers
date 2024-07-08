import sys
S = sys.stdin.readline().strip()
answer = []
check = []
isForward = False
for x in S:
    if x == '<':
        isForward = True
        if check:
            answer.append(check[::-1])
            check = []
        check.append(x)
    elif x == '>':
        isForward = False
        check.append(x)
        answer.append(check)
        check = []
    elif x == ' ' and not isForward:
        check = check[::-1]
        check.append(' ')
        answer.append(check)
        check = []
    else:
        check.append(x)
if check:
    answer.append(check[::-1])
result = ''
for a in answer:
    result += ''.join(a)
print(result)