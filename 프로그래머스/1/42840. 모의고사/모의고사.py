def solution(answers):
    answer = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if first[i % len(first)] == answers[i]:
            answer[0] += 1
        if second[i % len(second)] == answers[i]:
            answer[1] += 1
        if third[i % len(third)] == answers[i]:
            answer[2] += 1
    max_num = 0
    max_arr = []
    for i,a in enumerate(answer):
        if a > max_num:
            max_arr = [i+1]
            max_num = a
        elif a == max_num:
            max_arr.append(i+1)
    return max_arr