def solution(babbling):
    answer = 0
    not_ = ["ayaaya", "yeye", "woowoo", "mama"]
    yes = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for n in not_:
            if n in b:
                b = b.replace(n, 'x')
# 연속으로 나오는 거 먼저 모두 제거 (이 단계에서 하나씩 나오는 것도 제거하면 안됨)
        for y in yes:
            b = b.replace(y, ' ')
# 연속이 아니라 띄엄띄엄 나오는 단어들 모두 삭제 위해 그대로 사용
        b = b.replace(' ', '')
        if len(b) == 0:
            answer +=1
    
    return answer