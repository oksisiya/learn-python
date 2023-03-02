def solution(spell, dic):
    return 1 if ''.join(sorted(spell)) in [''.join(sorted(i)) for i in dic] else 2