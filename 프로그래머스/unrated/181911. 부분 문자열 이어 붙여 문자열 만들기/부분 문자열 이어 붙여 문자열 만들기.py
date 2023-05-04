def solution(my_strings, parts):
    return ''.join([my_strings[a][b[0]:b[1]+1] for a, b in enumerate(parts)])