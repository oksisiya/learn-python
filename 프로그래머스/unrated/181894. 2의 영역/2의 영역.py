def solution(arr):
    ls = []
    
    for idx, i in enumerate(arr):
        if i == 2: ls.append(idx)
        
    return arr[min(ls):max(ls) + 1] if len(ls) != 0 else [-1]