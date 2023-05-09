def solution(arr):
    answer = []
    
    for i in arr:
        j = 0
        
        while j != i:
            answer.append(i)
            j += 1
            
    return answer