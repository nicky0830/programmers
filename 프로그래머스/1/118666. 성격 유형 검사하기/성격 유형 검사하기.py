def solution(survey, choices):
    answer = ''
    mbti = ["R","T","C","F","J","M","A","N"]
    dic = {m:0 for m in mbti}
    for i,s in enumerate(survey):
        [minus, plus] = list(s)
        score = choices[i] - 4
        if score > 0:
            dic[plus] += score
        elif score < 0:
            dic[minus] -= score
    if dic.get('R') >= dic.get('T'):
        answer += 'R'
    else:
        answer += 'T'
    if dic.get('C') >= dic.get('F'):
        answer += 'C'
    else:
        answer += 'F'
    if dic.get('J') >= dic.get('M'):
        answer += 'J'
    else:
        answer += 'M'
    if dic.get('A') >= dic.get('N'):
        answer += 'A'
    else:
        answer += 'N'
    return answer
        
        
            
        
        
    
        
   