def solution(num_list):
    multiply = 1
    add = 0
    for n in num_list:
        multiply *= n
        add += n
    if multiply > add**2:
        return 0
    else:
        return 1