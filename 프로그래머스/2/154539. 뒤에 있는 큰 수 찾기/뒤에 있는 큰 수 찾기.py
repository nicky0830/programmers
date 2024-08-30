def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
            # 처리하지 않은 값들을 stack에 넣고
            # stack에 값이 있을 때까지 현재 i의 수를 계속 비교
        stack.append(i)
    return result