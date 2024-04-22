def solution(my_str, n):
    answer = []
    i=0 
    while i <= len(my_str):
        if my_str[i:i+n] != '':
            answer.append(my_str[i:i+n])
        i = i+n
    return answer