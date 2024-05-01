def solution(emergency):
    answer = []
    sorted_list = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(sorted_list.index(e)+1)
    return answer