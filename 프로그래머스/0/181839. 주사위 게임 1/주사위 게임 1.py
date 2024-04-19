def solution(a, b):
    def isOdd(num): 
        if num % 2 != 0:
            return True
    if isOdd(a) and isOdd(b):
        return a**2 + b**2
    elif not isOdd(a) and not isOdd(b):
        return abs(a - b)
    else:
        return 2 * (a+b)