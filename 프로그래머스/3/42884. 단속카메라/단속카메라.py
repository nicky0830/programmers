def solution(routes):
    routes.sort(key=lambda x: x[0])
    last_end = routes[0][1]
    answer=1
    for route in routes[1:]:
        [start, end] = route
        if start > last_end:
            answer += 1
            last_end = end
        else:
            if last_end > end:
                last_end = end
    return answer