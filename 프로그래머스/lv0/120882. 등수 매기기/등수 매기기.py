def solution(score):
    ls = []
    answer = []
    
    for i in score:
        ls.append(sum(i)/len(i))
    
    lss = sorted(ls, reverse = True)
    
    for i in ls:
        if i in lss: answer.append(lss.index(i)+1)
        
    return answer