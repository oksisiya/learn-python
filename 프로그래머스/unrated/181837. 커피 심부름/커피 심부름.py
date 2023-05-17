def solution(order):
    answer = 0
    
    for i in order:
        if 'americano' in i: answer += 4500
        if 'cafelatte' in i: answer += 5000
        if i == 'anything': answer += 4500
        
    return answer