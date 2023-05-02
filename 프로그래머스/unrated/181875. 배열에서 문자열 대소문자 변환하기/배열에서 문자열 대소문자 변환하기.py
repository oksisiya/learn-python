def solution(strArr):
    return [i.upper() if strArr.index(i) % 2 != 0 else i.lower() for i in strArr]