def solution(arr):
    check =''
    answer = []
    for a in arr:
        if answer[-1:] == [a]: continue
#         -1이면 range를 벗어나니까 비교 대상을 둘 다 배열로 만들어준다
        answer.append(a)
    return answer
            
 