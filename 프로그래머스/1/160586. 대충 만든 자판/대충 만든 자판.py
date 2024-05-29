def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dic:
                dic[k] = i+1
            else:
                if dic[k] > i+1:
                    dic[k] = i+1
    for target in targets:
        count = 0
        for t in target:
            if t not in dic:
                count =-1
                break
            else:
                count += dic[t]
        answer.append(count)
    return answer