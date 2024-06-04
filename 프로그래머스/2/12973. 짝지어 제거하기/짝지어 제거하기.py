def solution(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    if len(stack) > 0:
        return 0
    else:
        return 1
            