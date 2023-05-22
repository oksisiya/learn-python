def solution(arr, flag):
    answer = []
    
    for idx, i in enumerate(flag):
        if i:
            answer += [arr[idx] for i in range(arr[idx] * 2)]
        else:
            for i in range(arr[idx]): answer.pop()
            
    return answer