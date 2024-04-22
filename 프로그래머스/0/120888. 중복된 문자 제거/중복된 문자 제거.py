def solution(my_string):
    check = set()
    answer = ''
    for m in my_string:
        if m not in check:
            answer += m
            check.add(m)
    return answer
            