def solution(babbling):
    answer = 0
    sound = ['aya', 'ye', 'woo', 'ma']
    wrong_bable = ['ayaaya', 'yeye', 'woowoo', 'mama']
    
    for b in babbling:
        for w in wrong_bable:
            if w in b:
                b = 'X'
        for s in sound:
            b = b.replace(s, ' ')
        b = b.replace(' ', '')
        if len(b) == 0:
            answer+=1
    return answer