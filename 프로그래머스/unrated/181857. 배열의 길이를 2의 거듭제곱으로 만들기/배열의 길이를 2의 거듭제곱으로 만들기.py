import math

def solution(arr):
    while len(arr) != 2 ** math.ceil(math.log2(len(arr))):
        arr.append(0)

    return arr