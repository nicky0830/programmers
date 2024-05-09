def solution(n, slicer, num_list):
    answer = []
    a,b,c = slicer
    if n==1:
        return num_list[:b+1]
    if n==2:
        return num_list[a:]
    if n==3:
        return num_list[a:b+1]
    if n==4:
        idx = 0
        new_list = num_list[a:b+1]
        while idx < len(new_list):
            print(idx)
            answer.append(new_list[idx])
            idx += c
        return answer