def solution(n_str):
    for i in n_str:
        if i == str(0): pass
        else: return n_str[n_str.index(i):]