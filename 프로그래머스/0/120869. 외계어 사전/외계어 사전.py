def solution(spell, dic):
    for d in list(filter(lambda x: len(x) == len(spell),dic)):
        if set(spell) & set(d) == set(spell):
            return 1
    return 2