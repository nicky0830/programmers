def solution(answers):
    answer = []
    one, two, three = 0, 0, 0
    oneArr = [1,2,3,4,5]
    twoArr = [2,1,2,3,2,4,2,5]
    threeArr = [3,3,1,1,2,2,4,4,5,5]
    for i,a in enumerate(answers):
        if oneArr[i%5] == a:
            one += 1
        if twoArr[i%8] == a:
            two += 1
        if  threeArr[i%10] == a:
            three += 1
    max_count = max(one, two, three)
    
    indices=[]
    
    for i, count in enumerate([one, two, three]):
        if count == max_count:
            indices.append(i+1) 
    return indices