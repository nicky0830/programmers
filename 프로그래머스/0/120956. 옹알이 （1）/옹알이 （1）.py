def solution(babbling):
    answer = 0
    sounds = [ "aya", "ye", "woo", "ma" ]
    for b in babbling:
        for s in sounds:
            if s in b:
                b = b.replace(s, ' ')
       	b = b.replace(' ', '')
        if len(b) == 0:
            answer += 1
    return answer