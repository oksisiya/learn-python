def solution(num_list):
    even = []
    odd = []
    
    for idx, i in enumerate(num_list):
        even.append(i) if idx % 2 == 0 else odd.append(i)
        
    return max(sum(even), sum(odd))