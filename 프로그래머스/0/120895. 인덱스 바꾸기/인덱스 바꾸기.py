def solution(my_string, num1, num2):
    answer = ''
    first = my_string[num1]
    second = my_string[num2]
    for i,e in enumerate(my_string):
        if i == num1:
            answer += second
        elif i == num2: 
            answer += first
        else:
            answer += e   
    return answer