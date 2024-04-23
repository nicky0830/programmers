def solution(s):
    answer = True
    stack = []
    for e in s:
        if e == '(':
            stack.append(e)
        elif stack:
            stack.pop()
        else:
            return False
    return not bool(len(stack))