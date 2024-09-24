def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0