def solution(arr):
    for idx, i in enumerate(arr):
        if i >= 50 and i % 2 == 0: arr[idx] =  i / 2
        if i < 50 and i % 2 != 0: arr[idx] = i * 2
        
    return arr