def solution(s):
    answer = 0
    ll = len(s)
    left = '({['
    right = ')}]'
    s = s*2
    for i in range(ll):
        new_s = s[i:i+ll]
        stack = []
        for x in new_s:
            if x in left:
                stack.append(left.index(x))
            else:
                if not stack:
                    stack.append('null')
                    continue
                elif stack[-1] == right.index(x):
                    stack.pop()
        if len(stack) == 0:
            answer += 1
    return answer