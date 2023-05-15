def solution(myString, pat):
    if pat[::-1] in myString[::-1]:
        num = myString[::-1].index(pat[::-1])

    return myString[:len(myString) - num]