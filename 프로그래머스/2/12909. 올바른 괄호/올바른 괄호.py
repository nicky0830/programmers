def solution(s):
    answer = True
    stack = []
    for e in s:
        if e == '(':
            stack.append(e)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return not bool(len(stack))