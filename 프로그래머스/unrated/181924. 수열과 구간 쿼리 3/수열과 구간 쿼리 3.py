def solution(arr, queries):
    for i in queries:
        x = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = x
    
    return arr