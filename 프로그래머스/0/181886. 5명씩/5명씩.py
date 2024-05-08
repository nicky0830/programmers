def solution(names):
    answer = []
    check = 0
    while check < len(names):
        answer.append(names[check])
        check += 5
    return answer