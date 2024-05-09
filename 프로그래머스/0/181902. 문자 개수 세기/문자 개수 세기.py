def solution(my_string):
    answer = [0]*52
    A = ord('A')
    a = ord('a')
    print(A,a)
    for m in my_string:
        if ord(m) >= a:
            answer[ord(m)-a+26] += 1
        else:
            answer[ord(m)-A] += 1
    return answer