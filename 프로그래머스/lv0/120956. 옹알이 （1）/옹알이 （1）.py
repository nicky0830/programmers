def solution(babbling):
# 1. find로 인덱스 찾기 
# 2. 제거하기 
# 3. 나머지에서 반복
    answer =0
    check = ["aya", "ye", "woo", "ma"]
    check.sort()
    babbling.sort()
    for b in babbling:
        for c in check:
            if b.find(c) != -1: 
                b = b.replace(c, '1')
                print(b)
        if b.isdigit():
            answer = answer+1
    return answer