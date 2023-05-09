def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        answer.append([j for j in arr[queries[i][0]:queries[i][1]+1] if j > queries[i][2]])
        if len(answer[i]) == 0: answer[i].append(-1)
        
    return [min(i) for i in answer]