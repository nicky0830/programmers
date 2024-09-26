def solution(priorities, location):
    len_ = len(priorities)
    answer = [-1] * len_
    idx=0
    rate=1
#   max인지 확인하기
#   아닌 거 확인하기
    while answer[location] == -1:
        if priorities[idx] == max(priorities):
            priorities[idx] = -1
            answer[idx] = rate
            rate += 1
        idx += 1
        idx %= len_
    return answer[location]