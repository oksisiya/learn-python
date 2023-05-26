# def solution(q, r, code):
#     answer = ''
    
#     for i in code:
#         if code.index(i) % q == r: answer += i
    
#     return answer

# def solution(q, r, code):
#     return ''.join([i for i in code if code.index(i) % q == r])

def solution(q, r, code):
    answer = ''
    
    for idx, i in enumerate(code):
        if idx % q == r: answer += i
    
    return answer