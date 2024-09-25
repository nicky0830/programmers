def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0 for _ in range(bridge_length)]
    sum_q = 0
    while True:
        answer += 1
        sum_q -= q[0]
        q.pop(0)
        if truck_weights and sum_q + truck_weights[0] <= weight:
            sum_q += truck_weights[0]
            q.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            q.append(0)
        if not truck_weights:
            answer += bridge_length
            return answer