import re
def solution(my_string):
    return sum(map(int,list(filter(lambda x: x!='', re.split('[^0-9]', my_string)))))
