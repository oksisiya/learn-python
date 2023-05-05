def solution(myString, pat):
    ls = []
    
    for i in myString:
        a = lambda i: 'A' if i == 'B' else 'B'
        ls.append(a(i))
        
    return 1 if pat in ''.join(ls) else 0