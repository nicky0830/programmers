def solution(arr):
    check =''
    answer = []
    for a in arr: 
        if answer[-1:] == [a]: continue
        answer.append(a)
    return answer
            
 