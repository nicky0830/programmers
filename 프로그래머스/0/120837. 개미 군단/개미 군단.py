def solution(hp):
    answer = 0
#     장군 5, 병정 3, 일개미 1
    answer += hp//5
    hp = hp % 5
    answer += hp//3
    hp = hp % 3
    answer += hp
    return answer