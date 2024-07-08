import sys
s = sys.stdin.readline()
stack = []
answer = 0
for i, e in enumerate(list(s)):
    if e == '(':
        stack.append(i)
    if e == ')':
        top = stack.pop()
        if i == top+1:
            answer += len(stack)
        else:
            answer += 1
print(answer)