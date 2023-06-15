def solution(arr):
    check =''
    answer = []
    for a in arr: 
        if check != a:
            answer.append(a)
            check = a  
    return answer
            
 