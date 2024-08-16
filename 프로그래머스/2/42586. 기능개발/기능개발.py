import math
def solution(progresses, speeds):
    answer = []
    left_days = []
    for i in range(len(progresses)):
        left_days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    max_day = left_days[0]
    q = [max_day]
    for l in left_days[1:]:
        if l > max_day:
            max_day = l
            if q:
                answer.append(len(q))
            q = [max_day]
        else:
            q.append(l)
    answer.append(len(q))
    return answer
