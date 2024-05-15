def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for a in s:
        if a.isalpha():
            return False
    return True
