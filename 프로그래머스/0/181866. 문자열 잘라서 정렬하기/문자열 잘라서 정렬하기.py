def solution(myString):
    answer = []
    return sorted(list(filter(lambda x: x != '', myString.split("x"))))