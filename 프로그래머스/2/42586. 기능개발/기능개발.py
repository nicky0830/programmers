import math 
def solution(progresses, speeds):
    answer = []
    leftdays = []
    for i,e in enumerate(progresses):
        leftday = math.ceil((100 - e)/speeds[i])
        leftdays.append(leftday)
    maxDay = leftdays[0]
    count = 0
    for i,day in enumerate(leftdays):
        if day > maxDay:
            answer.append(count)
            maxDay = day
            count = 1
        else:
            count += 1
        if i == len(leftdays)-1:
            answer.append(count)
    return answer
            
            
            
    
        