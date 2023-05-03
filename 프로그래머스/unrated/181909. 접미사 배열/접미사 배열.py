def solution(my_string):
    ls = []
    
    for i in range(len(my_string)):
        ls.append(my_string[:i + 1])
        
    return sorted(ls)